from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", indexView.as_view(),name="index"),
    path("contato/", contato_listView.as_view(),name="contato"),
    path("grupo/",grupo_listView.as_view(),name="grupo"),
    path("telefone/",telefone_listView.as_view(),name="telefone"),
    path("email/",email_listView.as_view(),name="email"),
    path("usuario/",usuario_listView.as_view(),name="usuario"),
    path("pesquisa/",pesquisa_listView.as_view(),name="pesquisa"),
    path("chamada/",chamada_listView.as_view(),name="chamada"),
]