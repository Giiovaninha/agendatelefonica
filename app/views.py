from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def contatos_list_view(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos_list.html', {'contatos':contatos})

def editar_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if request.method == 'POST':
        form = EditarContatoForm(request.POST, id=contato_id)
        if form.is_valid():
            cd = form.cleaned_data
            contato.nome = cd['nome_contato']
            contato.save() 

            cd_grupos = []
            cd_tels = []
            cd_email = []

            for nome, valor in cd.items():
                if nome.startswith('tel_'):
                    cd_tels.append(valor)
                elif nome.startswith('emails_'):
                    cd_email.append(valor)
                elif nome.startswith('g_'):
                    if valor:
                        grupo = Grupo.objects.get(nome=nome.replace('g_', ''))
                        cd_grupos.append(grupo)

            contato_tels = contato.telefone_set.all()
            contato_emails = contato.email_set.all()
            contato_grupos = contato.grupos.all()

            for i, tel in enumerate(contato_tels):
                if i < len(cd_tels):
                    tel.numero = cd_tels[i]
                    tel.save()
                else:
                    tel.delete()  

            for i, email in enumerate(contato_emails):
                if i < len(cd_email):
                    email.descricao = cd_email[i]
                    email.save()
                else:
                    email.delete()  

            for grupo in cd_grupos:
                if grupo not in contato_grupos:
                    contato.grupos.add(grupo)

            for grupo in contato_grupos:
                if grupo not in cd_grupos:
                    contato.grupos.remove(grupo)
            
            return redirect('contatos_list_view')
    else:
        form = EditarContatoForm(instance=contato)
    
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
            return redirect('editar_contato', contato_id=contato.id)
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
            return redirect('editar_contato', contato_id=contato.id)
    else:
        form = NovoEmailForm()
    return render(request, 'novo_email.html', {'form':form, 'contato':contato})

def excluir_contato_view(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    contato.delete()
    return redirect('contatos_list_view')

def excluir_telefone_view(request, contato_id, label):
    contato = get_object_or_404(Contato, id=contato_id)
    telefone_seq = int(label.replace('Telefone ', '')) - 1
    telefone = contato.telefone_set.all()[telefone_seq]
    telefone.delete()
    return redirect('editar_contato', contato_id=contato.id)

def excluir_email_view(request, contato_id, label):
    contato = get_object_or_404(Contato, id=contato_id)
    email_seq = int(label.replace('Email ', '')) - 1
    email = contato.email_set.all()[email_seq]
    email.delete()
    return redirect('editar_contato', contato_id=contato.id)







