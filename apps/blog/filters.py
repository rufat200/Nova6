from django_filters import rest_framework as filters

from .models import Category, Publication


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Category
        fields = ['name']

class PublicationFilter(filters.FilterSet):
    content =  filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Publication
        fields = ['user','category','content']