from django_filters.rest_framework import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
            'user': ['exact'],
            'product_type': ['exact'],
            'created_date': ['gt','lt'],

        }