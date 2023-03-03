from rest_framework import serializers
from order.models import order, orderItem

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = order
        fields = '__all__'
        depth = 1


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = orderItem
        fields = '__all__'
        depth = 1