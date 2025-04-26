from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from users.permissions import IsCustomerUser, IsVendorUser


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()   # ✅ ADD THIS LINE
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'customer':
            return Order.objects.filter(customer=user)
        elif user.role == 'vendor':
            return Order.objects.filter(items__product__vendor__user=user).distinct()
        elif user.role == 'admin':
            return Order.objects.all()
        return Order.objects.none()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
