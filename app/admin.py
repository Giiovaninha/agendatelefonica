from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(models.Grupo)
admin.site.register(models.Contato)
admin.site.register(models.Telefone)
admin.site.register(models.Email)
admin.site.register(models.Usuario)
admin.site.register(models.Pesquisa)
admin.site.register(models.Chamada)