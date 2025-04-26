from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created_at', 'items']
        read_only_fields = ['customer', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(customer=self.context['request'].user, **validated_data)
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order
