from django.urls import path
from .views import buscar_rubros, process_id

urlpatterns = [
    path('buscar/', buscar_rubros, name='buscar_rubros'),
    path('procesar/', process_id, name='procesar_id'),
]
