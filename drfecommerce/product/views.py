from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from .models import *
from .serializers import *

# Create your views here.

class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or Brand users.
    """

    serializer_class = BrandSerializer
    @extend_schema(request=BrandSerializer)
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Brand.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = BrandSerializer(user)
    #     return Response(serializer.data)


class CategoriesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or Categories users.
    """

    serializer_class = CategoriesSerializer
    @extend_schema(request=CategoriesSerializer)
    def list(self, request):
        queryset = Categories.objects.all()
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Categories.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = CategoriesSerializer(user)
    #     return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or Product users.
    """
    queryset = Product.objects.all()

    @action(
        detail=False,
        methods=['get'],
        url_path='(?P<category>[^/.]+)/all',
    )
    def list_product_by_category(self, request, category = None):
        serialized = ProductSerializer(self.queryset.filter(categories__name=category),many=True)
        return Response(serialized.data)

    serializer_class = ProductSerializer
    @extend_schema(request=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Product.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = ProductSerializer(user)
    #     return Response(serializer.data)