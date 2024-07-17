from django.db import models

# Create your models here.
class Grupo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=280, null=True, blank=True)

class Contato(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    sobrenome = models.CharField(max_length=50, unique=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    grupos = models.ManyToManyField(Grupo)
    cpf = models.CharField(max_length=14)  # Ajustei o max_length para CPF padrão

    class Meta:
        ordering = ['nome']

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    contatos = models.ForeignKey(Contato, on_delete=models.CASCADE)

class Email(models.Model):
    endereco = models.EmailField(max_length=255)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    senha = models.CharField(max_length=128)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)

class Pesquisa(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Chamada(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    duracao = models.DurationField()  