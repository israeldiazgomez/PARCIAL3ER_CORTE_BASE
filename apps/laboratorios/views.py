from django.shortcuts import render, redirect
from apps.laboratorios.models import Laboratorio
from apps.laboratorios.form import LaboratorioForm


def index(request):
    laboratorio = Laboratorio.objects.all().order_by('-id')
    context = {'laboratorios': laboratorio}
    return render(request, 'laboratorios/index.html', context)

def home(request):
    return render(request, 'base/base.html')

def laboratorioCreate(request):
    if(request.method == 'POST'):
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('laboratorios:index')
    else:
        form = LaboratorioForm()
        return render(request, 'laboratorios/formLaboratorio.html',{'form': form})

def laboratorioEdit(request, id_laboratorio):
    laboratorio = Laboratorio.objects.get(pk=id_laboratorio)
    
    if request.method == 'GET':
        form = LaboratorioForm(instance=laboratorio)  
    else:
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
        return redirect('laboratorios:index')
    return render(request, 'laboratorios/formLaboratorio.html', {'form': form})

def laboratorioDelete(request, id_laboratorio):
    laboratorio = Laboratorio.objects.get(pk=id_laboratorio)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorios:index')
    return render(request, 'laboratorios/laboratorioEliminar.html', {'laboratorios': laboratorio})