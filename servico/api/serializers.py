from rest_framework import serializers

from servico.models import Servico

class ServicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'