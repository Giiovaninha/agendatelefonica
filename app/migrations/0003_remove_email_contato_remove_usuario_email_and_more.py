# Generated by Django 5.0.7 on 2024-07-22 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_contatos_telefone_contato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='contato',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='contato',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='contato',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefone',
        ),
        migrations.AlterModelOptions(
            name='contato',
            options={},
        ),
        migrations.DeleteModel(
            name='Chamada',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Pesquisa',
        ),
        migrations.DeleteModel(
            name='Telefone',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
