# Generated by Django 3.2.4 on 2021-06-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, verbose_name='Descricao'),
        ),
    ]
