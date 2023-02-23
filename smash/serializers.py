from rest_framework import serializers
from .models import Products, ProductsCategory, Product, Cart, User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['__all__']


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['__all__']


class ProductsCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategory
        fields = ['__all__']


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['__all__']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['__all__']
