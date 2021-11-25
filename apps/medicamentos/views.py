from django.db import models
from django.shortcuts import render, redirect
from apps.medicamentos.models import Medicamento
from apps.medicamentos.form import MedicamentoForm


def index(request):
    medicamento = Medicamento.objects.all().order_by('-id')
    context = {'medicamentos': medicamento}
    return render(request, 'medicamentos/index.html', context)

def home(request):
    return render(request, 'base/base.html')

def medicamentoCreate(request):
    if(request.method == 'POST'):
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('medicamentos:index')
    else:
        form = MedicamentoForm()
        return render(request, 'medicamentos/formMedicamento.html',{'form': form})

def medicamentoEdit(request, id_medicamento):
    medicamento = Medicamento.objects.get(pk=id_medicamento)
    
    if request.method == 'GET':
        form = MedicamentoForm(instance=medicamento)  
    else:
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
        return redirect('medicamentos:index')
    return render(request, 'medicamentos/formMedicamento.html', {'form': form})

def medicamentoDelete(request, id_medicamento):
    medicamento = Medicamento.objects.get(pk=id_medicamento)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamentos:index')
    return render(request, 'medicamentos/medicamentoEliminar.html', {'medicamentos': medicamento})