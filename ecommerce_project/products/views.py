from django.core.cache import cache
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from users.permissions import IsVendorUser, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['price', 'stock']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'stock']

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Product.objects.all()
        elif user.role == 'vendor':
            return Product.objects.filter(vendor__user=user)
        return Product.objects.none()

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user.vendor_profile)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Product.objects.all()
        elif user.role == 'vendor':
            return Product.objects.filter(vendor__user=user)
        elif user.role == 'customer':
            cache_key = 'customer_products'
            products = cache.get(cache_key)
            if not products:
                products = list(Product.objects.all())
                cache.set(cache_key, products, timeout=60*5)  # cache for 5 minutes
            return products
        return Product.objects.none()    