from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from product.models import product, productDetail
from product.serializers import ProductSerializer,ProductDetailSerializer
from django.http import JsonResponse

# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import AllowAny


class ProductViewSet(GenericViewSet,ListModelMixin):

    queryset = product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)


class ProductDetailViewSet(GenericViewSet,RetrieveModelMixin):

    queryset = productDetail.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, pk):
        try:
            return self.retrieve(request,pk)
        except:
            response = JsonResponse({"error message": "something wrong with searched id"})
            response.status_code = 404
            return response
