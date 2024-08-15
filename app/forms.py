from django import forms
from .models import *

class EditarContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'sobrenome', 'foto']  # Inclua os campos do modelo que você deseja exibir no formulário

    def __init__(self, *args, **kwargs):
        contato_id = kwargs.pop('id', None)
        if contato_id is None:
            raise ValueError("O ID do contato deve ser fornecido.")
        contato = Contato.objects.get(id=contato_id)
        super().__init__(*args, **kwargs)
        self.fields['nome'].initial = contato.nome
        self.fields['sobrenome'].initial = contato.sobrenome
        self.fields['foto'].initial = contato.foto

        grupos = Grupo.objects.all()
        grupos_contato = contato.grupos.all()

        for grupo in grupos:
            self.fields[f"g_{grupo.nome}"] = forms.BooleanField(required=False, initial=grupo in grupos_contato, label=f"{grupo.nome}")

        for i, tel in enumerate(contato.telefone_set.all()):
            self.fields[f"tel_{i}"] = forms.CharField(max_length=14, label=f"Telefone {i+1}", initial=tel.numero)

        for i, email in enumerate(contato.email_set.all()):
            self.fields[f"email_{i}"] = forms.EmailField(max_length=255, label=f"Email {i+1}", initial=email.endereco)

    def clean_nome(self):
        nome_contato = self.cleaned_data.get('nome')

        nomes_contatos = [contact.nome for contact in Contato.objects.exclude(id=self.instance.id)]
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