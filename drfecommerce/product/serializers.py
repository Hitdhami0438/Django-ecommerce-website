from rest_framework import serializers
from .models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    categories_name = serializers.CharField(source='categories.name')
    product_line = ProductLineSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id',
                'name',
                'description',
                'brand_name',
                'categories_name',
                'product_line'
            )