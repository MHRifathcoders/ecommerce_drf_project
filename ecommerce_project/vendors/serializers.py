from rest_framework import serializers
from .models import Vendor
from users.serializers import UserSerializer

class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Vendor
        fields = ['id', 'user', 'shop_name']
