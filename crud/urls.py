# SUGESTÃO (mais consistente)
from django.urls import path
# Renomeie as views 'delete' para 'apagar' e 'update' para 'atualizar' no seu views.py
from .views import home, salvar, apagar, editar, atualizar

urlpatterns = [
    path('', home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('apagar/<int:id>/', apagar, name='apagar'),      # Tudo em português
    path('editar/<int:id>/', editar, name='editar'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'), # Tudo em português
]