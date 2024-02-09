from rest_framework import viewsets
from rpm_service.models import ConnectivityTypeModel
from rpm_service.serializers.ConnectivityType import ConnectivityTypeSerializer



class ConnectivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ConnectivityTypeModel.objects.all()
    serializer_class = ConnectivityTypeSerializer
  
