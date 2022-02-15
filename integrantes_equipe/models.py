from django.db import models

# Create your models here.

class Integrantes_Equipe(models.Model):
    id_integrante_equipe = models.AutoField(primary_key=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    nome_integrante_equipe = models.CharField(max_length=100,blank=False,null=False)
    data_nascimento = models.DateTimeField(blank=False,null=False)
    uf = models.CharField(max_length=2,blank=False,null=False)
    cep = models.CharField(max_length=100,blank=False,null=False)
    numero_logradouro = models.CharField(max_length=100,blank=False,null=True)
    complemento = models.CharField(max_length=100,blank=False,null=True)
    admin = models.BooleanField(default=False)
    cargo = models.CharField(max_length=100,blank=False,null=True)
    cpf_cnpj = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'integrantes_equipe'
        unique_together =  ('cpf_cnpj','id_integrante_equipe')
