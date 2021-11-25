from django.urls import path, include
from apps.medicamentos.views import index,medicamentoCreate,medicamentoDelete,medicamentoEdit
app_name = "medicamentos"; 

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', medicamentoCreate, name='medicamentoCreate'),
    path('actualizar/<int:id_medicamento>/', medicamentoEdit, name='medicamentoEdit'),
    path('eliminar/<int:id_medicamento>/', medicamentoDelete, name='medicamentoDelete'),
]