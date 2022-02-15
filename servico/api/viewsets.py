from rest_framework import viewsets

from servico.models import Servico
from servico.api.serializers import ServicoSerializers

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializers