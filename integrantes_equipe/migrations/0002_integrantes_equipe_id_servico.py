# Generated by Django 4.0.2 on 2022-02-15 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0001_initial'),
        ('integrantes_equipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrantes_equipe',
            name='id_servico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='integrantes_equipes', to='servico.servico'),
        ),
    ]
