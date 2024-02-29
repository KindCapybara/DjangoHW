from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProductViewSet(filters.FilterSet):
    class Meta:
        model = Product
        search_fields = ['title', 'description']


class StockViewSet(filters.FilterSet):
    class Meta:
        model = Stock
        filter_fields = ['address', 'products']
