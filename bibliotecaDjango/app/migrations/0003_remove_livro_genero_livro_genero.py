# Generated by Django 4.2.5 on 2023-09-25 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_leitores_leitor_emprestimo_data_devolucao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='genero',
        ),
        migrations.AddField(
            model_name='livro',
            name='genero',
            field=models.ManyToManyField(to='app.genero'),
        ),
    ]
