from rest_framework import serializers
from .models import CatalogAnalysis
from .models import Product
from .models import Category
from .models import Seller


class CatalogAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogAnalysis
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

