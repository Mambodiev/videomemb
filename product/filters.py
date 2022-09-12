from .models import Product
import django_filters
from django_filters.widgets import RangeWidget


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label="Search", lookup_expr='icontains')
    last_seen = django_filters.DateFromToRangeFilter(label="Created Between", widget=RangeWidget(attrs={'type': 'date'}))
    product_cost =  django_filters.RangeFilter(label="Price range")
    age =  django_filters.RangeFilter()
    likes =  django_filters.RangeFilter()
    comment =  django_filters.RangeFilter()
    class Meta:
        model = Product
        fields = {'title', 'age','likes', 'site_type', 'comment', 'gender', 'media_type', 'last_seen', 'technology', 'countries', 'language', 'button' ,'category','price',}
        
    