from django.urls import path
from .views import ProductListView, ProductDetailView, VideoDetailView, BlogListView
from django_filters.views import FilterView
from .filters import ProductFilter

app_name = "product"

urlpatterns = [
    # path("", ProductListView.as_view(), name='product-list'),
    path("", FilterView.as_view(filterset_class=ProductFilter,
        template_name='product/product_list.html'), name='product-list'),
    path("<slug>/", ProductDetailView.as_view(), name='product-detail'),
    path("<slug>/<video_slug>/", VideoDetailView.as_view(), name='video-detail'),
    path("blog", BlogListView.as_view(), name='blog-list'),
    
]