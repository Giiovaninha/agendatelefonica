from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Contato, Grupo, Telefone, Email, Usuario, Pesquisa, Chamada

def contatos_list_view(request):
    contatos = Contato.object.all()
    return render(request, 'contatos_list.html', {'contatos': contatos})

def contato_detail(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    return render(request, 'contato_detail.html', {'contato': contato})

def grupos_list(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupos_list.html', {'grupos': grupos})

def grupo_detail(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    return render(request, 'grupo_detail.html', {'grupo': grupo})

def telefones_list(request):
    telefones = Telefone.objects.all()
    return render(request, 'telefones_list.html', {'telefones': telefones})

def telefone_detail(request, pk):
    telefone = get_object_or_404(Telefone, pk=pk)
    return render(request, 'telefone_detail.html', {'telefone': telefone})

def emails_list(request):
    emails = Email.objects.all()
    return render(request, 'emails_list.html', {'emails': emails})

def email_detail(request, pk):
    email = get_object_or_404(Email, pk=pk)
    return render(request, 'email_detail.html', {'email': email})

def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios_list.html', {'usuarios': usuarios})

def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuario_detail.html', {'usuario': usuario})

def pesquisas_list(request):
    pesquisas = Pesquisa.objects.all()
    return render(request, 'pesquisas_list.html', {'pesquisas': pesquisas})

def pesquisa_detail(request, pk):
    pesquisa = get_object_or_404(Pesquisa, pk=pk)
    return render(request, 'pesquisa_detail.html', {'pesquisa': pesquisa})

def chamadas_list(request):
    chamadas = Chamada.objects.all()
    return render(request, 'chamadas_list.html', {'chamadas': chamadas})

def chamada_detail(request, pk):
    chamada = get_object_or_404(Chamada, pk=pk)
    return render(request, '/chamada_detail.html', {'chamada': chamada})


