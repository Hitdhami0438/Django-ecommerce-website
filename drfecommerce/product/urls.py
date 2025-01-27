from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register('brand', BrandViewSet, basename='brand')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]