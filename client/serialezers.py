from rest_framework import serializers
from smash.models import Products, ProductsCategory, Product, User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'location']
