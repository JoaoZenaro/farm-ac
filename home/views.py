from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests

from prestacao.models import Lancamentos, Prestacao

from django.db.models import Sum

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

import os, json
module_dir = os.path.dirname(__file__)

weather = 0
soil = 0
fire = 0

despesas = []
lucros = []
listaMeses = []


def dados():
    # Clima tempo -------------------------------------------------
    weatherPath = os.path.join(module_dir, 'testdata/weather.json')

    with open(weatherPath) as file:
        weather = json.load(file)

    # Solo ---------------------------------------------------------
    soilPath = os.path.join(module_dir, 'testdata/soil.json')

    with open(soilPath) as file:
        soil = json.load(file)

    # Alerta de fogo -----------------------------------------------
    firePath = os.path.join(module_dir, 'testdata/fire.json')

    with open(firePath) as file:
        fire = json.load(file)

    # ---------------------------------------------------------------

    weather = weather['data']
    soil = soil['data'][0]
    fire = fire['message']

    try:
        meses = Prestacao.objects.all().values('data').distinct()
    except:
        print('err')

    for i in range(len(meses)):
        listaMeses.append(str(meses[i]['data']))
        listaMeses[i].split(" ")
        listaMeses[i] = listaMeses[i][0:len(listaMeses[i])-3]

    prestacoes = Prestacao.objects.all().values_list('id', flat=True)

    for i in prestacoes:
        lucros.append(Lancamentos.objects.all().filter(prestacao=i,tipo=2))
        despesas.append(Lancamentos.objects.all().filter(prestacao=i,tipo=1))

    for i in range(len(prestacoes)):
        despesas[i] = despesas[i].aggregate(Sum('valor'))
        lucros[i] = lucros[i].aggregate(Sum('valor'))

        despesas[i] = despesas[i]['valor__sum']
        lucros[i] = lucros[i]['valor__sum']


# Create your views here.

def lancamentos_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=lancamentos_texto.txt'

	lancamentos = Lancamentos.objects.all()

	lines = []
	
	for l in lancamentos:
		lines.append(f'{l.nome}\n{l.descricao}\n{l.valor}\n{l.tipo}\n{l.data}\n{l.prestacao}\n\n\n')

	response.writelines(lines)
	return response
 
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required(login_url="/login/")
def index(request):
    
    dados()

    return render(request, "home/index.html", {
        'weather': weather,
        'fire': fire,
        'soil': soil
    })

def signup_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro efetuado!')
            return render(request, 'registration/signup.html', {'form': UserCreationForm(request.GET)})
        else:
            messages.error(request, 'Envio de formulário incorreto.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return listaMeses

    def get_providers(self):
        """Return names of datasets."""
        return ["Despesas", "Lucro"]

    def get_data(self):
        """Return 2 datasets to plot."""

        return [despesas,
                lucros]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()