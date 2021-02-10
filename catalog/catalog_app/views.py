from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CatalogAnalysisSerializer
from .models import CatalogAnalysis
from .serializers import ProductSerializer
from .models import Product
from .serializers import CategorySerializer
from .models import Category
from .serializers import SellerSerializer
from .models import Seller


class CatalogAnalysisViewSet(viewsets.ModelViewSet):
    queryset = CatalogAnalysis.objects.all().order_by('id')
    serializer_class = CatalogAnalysisSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all().order_by('id')
    serializer_class = SellerSerializer
