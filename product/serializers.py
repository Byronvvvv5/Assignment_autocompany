from rest_framework import serializers
from product.models import product, productDetail


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = productDetail
        fields = ['product_id', 'product_detail']
        depth = 1