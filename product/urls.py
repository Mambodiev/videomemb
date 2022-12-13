from django.urls import path
from .views import ProductListView, ProductDetailView, VideoDetailView, BlogListView
from django_filters.views import FilterView
from .filters import ProductFilter
from . import views

app_name = "product"

urlpatterns = [
    
    path("", FilterView.as_view(filterset_class=ProductFilter,
        template_name='product/product_list.html'), name='product-list'),
    path("<slug>/", ProductDetailView.as_view(), name='product-detail'),
    path('chart/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path("<slug>/<video_slug>/", VideoDetailView.as_view(), name='video-detail'),
    path("blog", BlogListView.as_view(), name='blog-list'),
    path('chart/sales/<int:year>/', views.get_sales_chart, name='chart-sales'),
    path('chart/spend-per-customer/<int:year>/', views.spend_per_customer_chart, name='chart-spend-per-customer'),
    path('chart/payment-success/<int:year>/', views.payment_success_chart, name='chart-payment-success'),
    path('chart/payment-method/<int:year>/', views.payment_method_chart, name='chart-payment-method'),
    
]