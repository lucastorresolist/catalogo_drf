from django.urls import include, path
from rest_framework import routers
from .views import CatalogAnalysisViewSet, ProductViewSet, SellerViewSet, CategoryViewSet 


router = routers.DefaultRouter()
router.register(r'catalogs', CatalogAnalysisViewSet, basename='catalogs')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'sellers', SellerViewSet, basename='seller')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'
    ))
]
