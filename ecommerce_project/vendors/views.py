from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Vendor
from .serializers import VendorSerializer
from users.permissions import IsAdminUser # type: ignore

class VendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
