from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from product.models import product, productDetail
from order.models import order, orderItem
from product.serializers import ProductSerializer,ProductDetailSerializer
from order.serializers import OrderSerializer, OrderItemSerializer
from django.http import JsonResponse


class OrderViewSet(GenericViewSet,ListModelMixin,UpdateModelMixin):

    queryset = order.objects.all()
    serializer_class = OrderSerializer

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().partial_update(request, *args, **kwargs)











