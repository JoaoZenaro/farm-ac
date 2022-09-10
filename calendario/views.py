from django.shortcuts import render, redirect
from .forms import CalendarioForm
from prestacao.models import Prestacao

from django.contrib import messages

# Create your views here.

def calendario_list(request):
    content = Prestacao.objects.all()

    return render(request, "calendario/calendario_list.html", {
        'calendario_list': content
    })


def calendario_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CalendarioForm()
        else:
            calendario = Prestacao.objects.get(pk=id)
            form = CalendarioForm(instance=calendario)
        return render(request, "calendario/calendario_form.html", {
                'form': form,
            })
    else:
        if id == 0:
            form = CalendarioForm(request.POST)
        else:
            calendario = Prestacao.objects.get(pk=id)
            form = CalendarioForm(request.POST,instance=calendario)
        if form.is_valid():
            form.save()
            messages.success(request, "Operação concluida.")
            return redirect('/linhadotempo/')
        else:
            messages.error(request, form.errors) 
        return redirect('/linhadotempo/list');

def calendario_delete(request,id):
    calendario = Prestacao.objects.get(pk=id)
    calendario.delete()
    return redirect('/linhadotempo/list')
