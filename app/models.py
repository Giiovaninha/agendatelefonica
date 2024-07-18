from django.db import models

class Grupo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=280, null=True, blank=True)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    sobrenome = models.CharField(max_length=50, unique=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    grupos = models.ManyToManyField(Grupo)
    cpf = models.CharField(max_length=14)  

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero

class Email(models.Model):
    endereco = models.EmailField(max_length=255)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)

    def __str__(self):
        return self.endereco

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    senha = models.CharField(max_length=128)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pesquisa(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pesquisa de {self.contato.nome} sobre {self.grupo.nome}"

class Chamada(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    duracao = models.DurationField()

    def __str__(self):
        return f"Chamada de {self.contato.nome} em {self.data} às {self.horario}"
