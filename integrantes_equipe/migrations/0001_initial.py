# Generated by Django 4.0.2 on 2022-02-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integrantes_Equipe',
            fields=[
                ('id_integrante_equipe', models.AutoField(primary_key=True, serialize=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('nome_integrante_equipe', models.CharField(max_length=100)),
                ('data_nascimento', models.DateTimeField()),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=100)),
                ('numero_logradouro', models.CharField(max_length=100, null=True)),
                ('complemento', models.CharField(max_length=100, null=True)),
                ('admin', models.BooleanField(default=False)),
                ('cargo', models.CharField(max_length=100, null=True)),
                ('cpf_cnpj', models.IntegerField()),
            ],
            options={
                'db_table': 'integrantes_equipe',
                'managed': True,
                'unique_together': {('cpf_cnpj', 'id_integrante_equipe')},
            },
        ),
    ]
