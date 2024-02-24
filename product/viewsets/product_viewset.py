from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")


# from rest_framework.viewsets import ModelViewSet
# from rest_framework.authentication import (
#     BasicAuthentication,
#     TokenAuthentication,
#     SessionAuthentication,
# )
# from rest_framework.permissions import IsAuthenticated
# from product.models import Product
# from product.serializers import ProductSerializer


# class ProductViewSet(ModelViewSet):
#     authentication_classes = [
#         BasicAuthentication,
#         TokenAuthentication,
#         SessionAuthentication,
#     ]
#     permission_classes = [IsAuthenticated]
#     serializer_class = ProductSerializer
#     # queryset = Product.objects.all()

#     def get_queryset(self):
#         return Product.objects.all().order_by("id")
