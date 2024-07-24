from django.shortcuts import render
from django.shortcuts import render
from .models import *
from django.views import View



class indexView(View):
    def get(self,request, *args,**kwargs):
        return render(request,'index.html')
    def post(self, request):
        pass 

class contato_listView(View):
    def get(self,request,*args,**kwargs):
        contato = Contato.objects.filter()
        usuarios = Usuario.objects.all()
        return render(request, 'contatos_list.html', {'contatos': contato, 'usuarios': usuarios})


class grupo_listView(View):
    def get(self,request,*args,**kwargs):
        grupo = Grupo.objects.all()
        return render(request, 'grupos_list.html', {'grupos': grupo})


class telefone_listView(View):
    def get(self,request,*args,**kwargs):
        telefone = Telefone.objects.all()
        return render(request, 'usuarios_list.html', {'telefone': telefone})



class email_listView(View):
    def get(self,request,*args,**kwargs):
        email = Email.objects.all()
        return render(request, 'emails_list.html', {'email': email})



class usuario_listView(View):
    def get(self,request,*args,**kwargs):
        usuario = Usuario.objects.all()
        return render(request, 'usuarios_list.html', {'usuario': usuario})



class pesquisa_listView(View):
    def get(self,request,*args,**kwargs):
        pesquisa = Pesquisa.objects.all()
        return render(request, 'pesquisas_list.html', {'pesquisa': pesquisa})


class chamada_listView(View):
    def get(self,request,*args,**kwargs):
        chamada = Chamada.objects.all()
        return render(request, 'chamadas_list.html', {'chamada': chamada})


