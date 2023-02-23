from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import ProductSerializers, ProductsSerializers, ProductsCategorySerializers
from .models import ProductsCategory, Products, Product

class ProductsCategoryViews(APIView):
    def get(self, request):
        products_category = ProductsCategory.objects.all()
        serializers = ProductsCategorySerializers(products_category, many=True)
        return Response(serializers.data)


class ProductsViews(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializers = ProductsSerializers(products, many=True)
        return Response(serializers.data)


class ProductViews(APIView):
    def get(self, request):
        product = Product.objects.filter(is_visible=True)
        serializers = ProductSerializers(product, many=True)
        return Response(serializers.data)











#
# class ProductsCategoryAPIViews(RetrieveUpdateDestroyAPIView):
#     """
#     get:
#         Returns the detail of a products category
#
#         parameters: [id]
#
#     put:
#         Update the detail of a products category
#
#         parameters: [id]
#
#     patch:
#
#         Update some fields of products category
#
#         parameters: [id]
#
#     delete:
#         Delete a products category
#
#         parameters: [id]
#     """
#
#     queryset = ProductsCategory.objects.all()
#     serializer_class = ProductsCategorySerializers
#
#
# class ProductsAPIViews(RetrieveUpdateDestroyAPIView):
#     """
#     get:
#         Returns the detail products
#
#         parameters: [id]
#
#     put:
#         Update the detail of products
#
#         parameters: [id]
#
#     patch:
#
#         Update some fields of products
#
#         parameters: [id]
#
#     delete:
#         Delete a products
#
#         parameters: [id]
#         """
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializers
#
#
# class ProductAPIViews(RetrieveUpdateDestroyAPIView):
#     """
#     get:
#         Returns the detail product
#
#         parameters: [id]
#
#     put:
#         Update the detail of product
#
#         parameters: [id]
#
#     patch:
#
#         Update some fields of product
#
#         parameters: [id]
#
#     delete:
#         Delete a product
#
#         parameters: [id]
#     """
#
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#
#
