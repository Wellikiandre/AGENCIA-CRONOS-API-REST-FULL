from rest_framework import serializers
from integrantes_equipe.models import  Integrantes_Equipe

class IntegrantesEquipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Integrantes_Equipe
        fields = '__all__'
