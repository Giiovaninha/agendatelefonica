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
from app.views import *

urlpatterns = [
    path("<int:pk>/", contato_list, name = 'contatos_list.html' ),
    path('<int:pk>/', grupo_list, name='grupos_list.html'),
    path('<int:pk>/', telefone_list, name='telefones_list.html'),
    path('<int:pk>/', email_list, name='emails_list.html'),
    path('<int:pk>/', usuario_list, name='usuarios_list.html'),
    path('<int:pk>/', pesquisa_list, name='pesquisas_list.html'),
    path('<int:pk>/', chamada_list, name='chamadas_list.html'),
]
