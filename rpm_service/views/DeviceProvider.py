from rest_framework import viewsets
from rpm_service.models import DeviceProviderModel
from rpm_service.serializers import DeviceProviderSerializer



class DeviceProviderViewSet(viewsets.ModelViewSet):
    queryset = DeviceProviderModel.objects.all()
    serializer_class = DeviceProviderSerializer
   

    