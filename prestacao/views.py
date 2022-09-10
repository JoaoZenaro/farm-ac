from django.shortcuts import render, redirect
from .forms import LancamentoForm
from .models import Lancamentos

from django.db.models import Sum

from django.contrib import messages

# Create your views here.

def lancamento_list(request):
    
    context = {
        'lancamento_list_despesas': Lancamentos.objects.all().filter(tipo=1).order_by('-data'),
        'lancamento_list_ganhos': Lancamentos.objects.all().filter(tipo=2).order_by('-data'),
        
    }
    return render(request, "prestacao/lancamento_list.html", context)


def lancamento_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = LancamentoForm()
        else:
            lancamento = Lancamentos.objects.get(pk=id)
            form = LancamentoForm(instance=lancamento)
        return render(request, "prestacao/lancamento_form.html", {
                'form': form
            })
    else:
        if id == 0:
            form = LancamentoForm(request.POST)
        else:
            lancamento = Lancamentos.objects.get(pk=id)
            form = LancamentoForm(request.POST,instance=lancamento)
        if form.is_valid():
            form.save()
            messages.success(request, "Operação concluida.")
            return redirect('/lancamento/list')
        else:
            messages.error(request, form.errors) 
        return redirect('/lancamento/');

def lancamento_delete(request,id):
    lancamento = Lancamentos.objects.get(pk=id)
    lancamento.delete()
    return redirect('/lancamento/list')
