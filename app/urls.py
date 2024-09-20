from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.contatos_list_view, name='contatos_list_view'),
    path('novo_grupo/', views.novo_grupo_view, name='novo_grupo'),
    path('contatos/<int:id>/editar/', views.editar_contato, name='editar_contato'),
    path('<int:contato_id>/novo_tel/', views.novo_tel_view, name='novo_tel'),
    path('<int:contato_id>/novo_email/', views.novo_email_view, name='novo_email'),
    path('<int:contato_id>/excluir/', views.excluir_contato_view, name='excluir_contato'),
    path('<int:contato_id>/telefone/<label>/excluir/', views.excluir_telefone_view, name='excluir_telefone'),
    path('<int:contato_id>/email/<label>/excluir/', views.excluir_email_view, name='excluir_email'),
    path('buscar/', views.buscar_contatos, name='buscar_contatos'),
    path('contatos/criar/', views.criar_contato, name='criar_contato'),
    path('grupos/criar/', views.criar_grupo, name='criar_grupo'),
    path('grupos/<int:id>/', views.detalhes_grupo, name='detalhes_grupo'),
    path('grupos/', views.lista_grupos, name='lista_grupos'),
    path('contatos/', views.lista_contatos, name='lista_contatos'),
    path('grupos/<int:id>/editar/', views.editar_grupo, name='editar_grupo'),
    path('grupos/<int:id>/excluir/', views.excluir_grupo, name='excluir_grupo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
