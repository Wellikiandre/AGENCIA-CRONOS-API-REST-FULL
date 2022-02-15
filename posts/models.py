from django.db import models
from integrantes_equipe.models import Integrantes_Equipe
# Create your models here.
class Posts(models.Model):
    id_post = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=100, blank=True, null=True)
    Conteudo = models.TextField(blank=True,null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_criacao_edt = models.DateTimeField(auto_now=True)
    conteudo_publico = models.BooleanField(default=True)
    id_integrante_equipe = models.ForeignKey(Integrantes_Equipe,on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'posts'