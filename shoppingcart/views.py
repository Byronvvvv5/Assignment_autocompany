from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from shoppingcart.models import shoppingCart, cartProducts
from shoppingcart.serializers import ShoppingCartSerializer, CartProductsSerializer
from django.http import JsonResponse


class ShoppingCartViewSet(GenericViewSet,ListModelMixin,CreateModelMixin,DestroyModelMixin):

    queryset = cartProducts.objects.all().order_by('id')
    serializer_class = CartProductsSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        try:
            return self.create(request)
        except:
            response = JsonResponse({"error message": "something wrong with entered information"})
            response.status_code = 500
            return response

    def delete(self, request, pk):
        return self.delete(request,pk)


