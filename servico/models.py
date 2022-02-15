from django.db import models

# Create your models here.
class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    tipo_servico = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'servico'