from rest_framework import viewsets, status
# from rest_framework.response import Response
# from common.exceptions import ValidationError
from rpm_service.models import DeviceModel
from rpm_service.serializers import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializer
    

    # def perform_create(self, serializer):
    #     serializer.save(organization_id=self.request.user_data.organization_id)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if not serializer.is_valid():
    #         raise ValidationError(str(serializer.errors))
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
