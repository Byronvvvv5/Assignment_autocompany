from rest_framework import serializers
from shoppingcart.models import shoppingCart, cartProducts


class ShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = shoppingCart
        fields = '__all__'
        depth = 1

class CartProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = cartProducts
        fields = '__all__'
        depth = 1
