from django import forms
from .models import *

class EditarContatoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        contato_id = kwargs.pop('id', None)  # Obtém 'id' ou define como None se não existir
        if contato_id is None:
            raise ValueError("O ID do contato deve ser fornecido.")
        contato = Contato.objects.get(id=contato_id)
        self.contato = contato
        super(EditarContatoForm, self).__init__(*args, **kwargs)
        self.fields['nome_contato'] = forms.CharField(max_length=50, initial=contato.nome)
        grupos = Grupo.objects.all()
        grupos_contato = contato.grupos.all()
        
        for grupo in grupos:
            self.fields[f"g_{grupo.nome}"] = forms.BooleanField(required=False, initial=grupo in grupos_contato, label=f"{grupo.nome}")

        for i, tel in enumerate(contato.telefone_set.all()):
            self.fields[f"tel_{i}"] = forms.CharField(max_length=14, label=f"Telefone {i+1}", initial=tel.numero)

        for i, email in enumerate(contato.email_set.all()):
            self.fields[f"email_{i}"] = forms.EmailField(max_length=255, label=f"Email {i+1}", initial=email.endereco)

    def clean_nome_contato(self):
        nome_contato = self.cleaned_data.get('nome_contato')

        nomes_contatos = [contact.nome for contact in Contato.objects.all() if contact.nome != self.contato.nome]
        if nome_contato in nomes_contatos:
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