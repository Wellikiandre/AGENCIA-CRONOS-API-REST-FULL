from rest_framework import viewsets
from integrantes_equipe.api.serializers import IntegrantesEquipeSerializers
from integrantes_equipe.models import Integrantes_Equipe

class IntegrantesEquipeViewSet(viewsets.ModelViewSet):
    queryset = Integrantes_Equipe.objects.all()
    serializer_class = IntegrantesEquipeSerializers