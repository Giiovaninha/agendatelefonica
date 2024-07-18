"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.contatos_list_view, name = 'contatos_list_view' ),
    path('grupos/', views.grupos_list, name='grupos_list'),
    path('grupos/<int:pk>/', views.grupo_detail, name='grupo_detail'),
    path('telefones/', views.telefones_list, name='telefones_list'),
    path('telefones/<int:pk>/', views.telefone_detail, name='telefone_detail'),
    path('emails/', views.emails_list, name='emails_list'),
    path('emails/<int:pk>/', views.email_detail, name='email_detail'),
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('pesquisas/', views.pesquisas_list, name='pesquisas_list'),
    path('pesquisas/<int:pk>/', views.pesquisa_detail, name='pesquisa_detail'),
    path('chamadas/', views.chamadas_list, name='chamadas_list'),
    path('chamadas/<int:pk>/', views.chamada_detail, name='chamada_detail'),
]
