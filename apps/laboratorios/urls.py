from django.urls import path, include
from apps.laboratorios.views import index,laboratorioCreate,laboratorioDelete,laboratorioEdit
app_name = "laboratorios"; 

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', laboratorioCreate, name='laboratorioCreate'),
    path('actualizar/<int:id_laboratorio>/', laboratorioEdit, name='laboratorioEdit'),
    path('eliminar/<int:id_laboratorio>/', laboratorioDelete, name='laboratorioDelete'),
]