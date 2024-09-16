from django import forms
from .models import *

from django.shortcuts import get_object_or_404

class EditarContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'sobrenome', 'foto']  

    def __init__(self, *args, **kwargs):
        contato_id = kwargs.pop('id', None)
        super().__init__(*args, **kwargs)
        if contato_id is None:
            raise ValueError("O ID do contato deve ser fornecido.")
        contato = get_object_or_404(Contato, id=contato_id)

        # Inicializa campos fixos
        self.fields['nome'].initial = contato.nome
        self.fields['sobrenome'].initial = contato.sobrenome
        self.fields['foto'].initial = contato.foto

        # Inicializa campos dinâmicos para grupos
        grupos = Grupo.objects.all()
        grupos_contato = contato.grupos.all()
        for grupo in grupos:
            self.fields[f"g_{grupo.id}"] = forms.BooleanField(
                required=False, 
                initial=grupo in grupos_contato, 
                label=f"{grupo.nome}"
            )

        # Inicializa campos dinâmicos para telefones e emails
        self._init_dynamic_fields(contato)

    def _init_dynamic_fields(self, contato):
        for i, tel in enumerate(contato.telefone_set.all()):
            self.fields[f"tel_{tel.id}"] = forms.CharField(
                max_length=14, 
                label=f"Telefone {i+1}", 
                initial=tel.numero
            )

        for i, email in enumerate(contato.email_set.all()):
            self.fields[f"email_{email.id}"] = forms.EmailField(
                max_length=255, 
                label=f"Email {i+1}", 
                initial=email.endereco
            )

    def save(self, commit=True):
        contato = super().save(commit=False)
        if commit:
            contato.save()
            self.save_m2m()  # Salva relações many-to-many (grupos)

            self._save_dynamic_fields(contato)
            contato.save()
        return contato

    def _save_dynamic_fields(self, contato):
        # Salva/Atualiza telefones
        for key, value in self.cleaned_data.items():
            if key.startswith("tel_"):
                tel_id = int(key.split("_")[1])
                telefone, created = Telefone.objects.get_or_create(contato=contato, id=tel_id)
                telefone.numero = value
                telefone.save()

        # Salva/Atualiza emails
        for key, value in self.cleaned_data.items():
            if key.startswith("email_"):
                email_id = int(key.split("_")[1])
                email, created = Email.objects.get_or_create(contato=contato, id=email_id)
                email.endereco = value
                email.save()

        # Atualiza grupos
        grupos = Grupo.objects.all()
        for grupo in grupos:
            field_name = f"g_{grupo.id}"
            if field_name in self.cleaned_data:
                if self.cleaned_data[field_name]:
                    contato.grupos.add(grupo)
                else:
                    contato.grupos.remove(grupo)

    def clean_nome(self):
        nome_contato = self.cleaned_data.get('nome')

        # Valida se o nome já existe, excluindo o contato atual
        if Contato.objects.exclude(id=self.instance.id).filter(nome=nome_contato).exists():
            raise forms.ValidationError("O nome escolhido já está sendo utilizado")
        return nome_contato



class NovoGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ('nome','descricao')

class NovoTelForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ('numero','contato')

class NovoEmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('endereco','contato')
        

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','sobrenome', 'foto', 'grupos']
        widgets = {
            'grupos': forms.CheckboxSelectMultiple()
        }

class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ['numero']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['endereco']

class CriarGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome']