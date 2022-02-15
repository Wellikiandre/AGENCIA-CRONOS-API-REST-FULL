# Generated by Django 4.0.2 on 2022-02-15 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('integrantes_equipe', '0002_integrantes_equipe_id_servico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('Conteudo', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_criacao_edt', models.DateTimeField(auto_now=True)),
                ('conteudo_publico', models.BooleanField(default=True)),
                ('id_integrante_equipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='integrantes_equipe.integrantes_equipe')),
            ],
            options={
                'db_table': 'posts',
                'managed': True,
            },
        ),
    ]
