from django.urls import path
from .views import ProductListView, ProductDetailView, VideoDetailView, BlogListView

app_name = "product"

urlpatterns = [
    path("", ProductListView.as_view(), name='product-list'),
    path("<slug>/", ProductDetailView.as_view(), name='product-detail'),
    path("<slug>/<video_slug>/", VideoDetailView.as_view(), name='video-detail'),
    path("blog", BlogListView.as_view(), name='blog-list'),
    
]