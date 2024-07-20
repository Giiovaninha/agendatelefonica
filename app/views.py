from django.shortcuts import render
from django.shortcuts import render
from .models import *


def base(request):
    return render(request,'template')

def contato_list_view(request):
    contato = Contato.objects.all()
    return render(request, 'app/contatos_list.html', {'contatos': contato})


# def grupo_list(request, pk):
#     grupo = get_object_or_404(Grupo, pk=pk)
#     return render(request, 'grupo_list.html', {'grupo': grupo})


# def telefone_list(request, pk):
#     telefone = get_object_or_404(Telefone, pk=pk)
#     return render(request, 'telefone_list.html', {'telefone': telefone})



# def email_list(request, pk):
#     email = get_object_or_404(Email, pk=pk)
#     return render(request, 'email_list.html', {'email': email})



# def usuario_list(request, pk):
#     usuario = get_object_or_404(Usuario, pk=pk)
#     return render(request, 'usuario_list.html', {'usuario': usuario})



# def pesquisa_list(request, pk):
#     pesquisa = get_object_or_404(Pesquisa, pk=pk)
#     return render(request, 'pesquisa_list.html', {'pesquisa': pesquisa})


# def chamada_list(request, pk):
#     chamada = get_object_or_404(Chamada, pk=pk)
#     return render(request, '/chamada_list.html', {'chamada': chamada})


