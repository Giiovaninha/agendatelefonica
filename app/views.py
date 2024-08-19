from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from .forms import *


def contatos_list_view(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos_list.html', {'contatos':contatos})

def editar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    if request.method == 'POST':
        form = EditarContatoForm(request.POST, id=id, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('contatos_list_view')
    else:
        form = EditarContatoForm(id=id, instance=contato)
    return render(request, 'editar_contato.html', {'form': form, 'contato': contato})



def novo_grupo_view(request):
    if request.method == 'POST':
        form = NovoGrupoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contatos_list_view')
    else:
        form = NovoGrupoForm()
    return render(request, 'novo_grupo.html', {'form':form})

def novo_tel_view(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if request.method == 'POST':
        form = NovoTelForm(data=request.POST)
        if form.is_valid():
            novo_tel = form.save(commit=False)
            novo_tel.contato = contato
            novo_tel.save()
            return redirect(reverse('editar_contato', kwargs={'id': contato_id}))
    else:
        form = NovoTelForm()
    return render(request, 'novo_tel.html', {'form':form, 'contato':contato})

def novo_email_view(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if request.method == 'POST':
        form = NovoEmailForm(data=request.POST)
        if form.is_valid():
            novo_email = form.save(commit=False)
            novo_email.contato = contato
            novo_email.save()
            return redirect(reverse('editar_contato', kwargs={'id': contato_id}))
    else:
        form = NovoEmailForm()
    return render(request, 'novo_email.html', {'form':form, 'contato':contato})

def excluir_contato_view(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    contato.delete()
    return redirect(reverse('contatos_list_view')) 

def excluir_telefone_view(request, contato_id, label):
    contato = get_object_or_404(Contato, id=contato_id)
    telefone_seq = int(label.replace('Telefone ', '')) - 1
    telefone = contato.telefone_set.all()[telefone_seq]
    telefone.delete()
    return redirect(reverse('editar_contato', kwargs={'id': contato_id}))

def excluir_email_view(request, contato_id, label):
    contato = get_object_or_404(Contato, id=contato_id)
    email_seq = int(label.replace('Email ', '')) - 1
    email = contato.email_set.all()[email_seq]
    email.delete()
    return redirect(reverse('editar_contato', kwargs={'id': contato_id}))

def buscar_contatos(request):
    query = request.GET.get('q', '')
    resultados = Contato.objects.filter(nome__icontains=query)
    return render(request, 'resultados_busca.html', {'resultados': resultados, 'query': query})

def detalhes_grupo(request, id):
    grupo = get_object_or_404(Grupo, id=id)
    return render(request, 'detalhes_grupo.html', {'grupo': grupo}) 

def criar_grupo(request):
    if request.method == 'POST':
        form = NovoGrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save()
            return redirect(reverse('detalhes_grupo', kwargs={'id': grupo.id}))
    else:
        form = NovoGrupoForm()
    return render(request, 'criar_grupo.html', {'form': form})


def editar_grupo(request, id):
    grupo = get_object_or_404(Grupo, id=id)
    
    if request.method == 'POST':
        form = NovoGrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect(reverse('detalhes_grupo', kwargs={'id': grupo.id}))
    else:
        form = NovoGrupoForm(instance=grupo)
    
    return render(request, 'editar_grupo.html', {'form': form, 'grupo': grupo})

def lista_grupos(request):
    grupos = Grupo.objects.all()  
    return render(request, 'lista_grupos.html', {'grupos': grupos})

def lista_contatos(request):
    contatos = Contato.objects.all()  
    return render(request, 'lista_contatos.html', {'contatos': contatos})

def criar_contato(request):
    if request.method == 'POST':
        contato_form = ContatoForm(request.POST, request.FILES)
        telefone_form = TelefoneForm(request.POST)
        email_form = EmailForm(request.POST)
        
        if contato_form.is_valid() and telefone_form.is_valid() and email_form.is_valid():
            contato = contato_form.save()
            
            telefone = telefone_form.save(commit=False)
            telefone.contato = contato
            telefone.save()
            
            email = email_form.save(commit=False)
            email.contato = contato
            email.save()
            
            return redirect('contatos_list_view')  
    else:
        contato_form = ContatoForm()
        telefone_form = TelefoneForm()
        email_form = EmailForm()

    
    return render(request, 'criar_contato.html', {
        'contato_form': contato_form,
        'telefone_form': telefone_form,
        'email_form': email_form,
    })











