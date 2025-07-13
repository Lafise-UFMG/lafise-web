from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('referencias/', views.referencias, name='referencias'),
    path('agenda/', views.agenda, name='agenda'),
    path('metodos-softwares/', views.metodos_softwares, name='metodos_softwares'),
    path('metodos/', views.metodos, name='metodos'),
    path('artigos/', views.artigos, name='artigos'),
    path('equipamentos/', views.equipamentos, name='equipamentos'),
    path('integrantes/', views.integrantes, name='integrantes'),
    path('grupo-cafezinho/', views.grupo_cafezinho, name='grupo_cafezinho'),
    path('historia/', views.historia, name='historia'),
    path('test-bootstrap/', views.test_bootstrap, name='test_bootstrap'),
]
