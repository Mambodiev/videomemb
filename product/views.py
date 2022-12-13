from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Product
from .filters import ProductFilter

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse
from django.shortcuts import render

from product.models import Purchase
from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict

class BlogListView(generic.ListView):
    template_name = "blog/blog_list.html"
    queryset = Product.objects.all()

class ProductListView(generic.ListView):
    template_name = "product/product_list.html"
    queryset = Product.objects.all()
    filter_set = ProductFilter
    
    




class ProductDetailView(generic.DetailView):
    template_name = "product/product_detail.html"
    queryset = Product.objects.all()


class VideoDetailView(generic.DetailView):
    template_name = "product/video_detail.html"

    # def get_object(self):
    #     video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
    #     return video

    def get_queryset(self):
        product = get_object_or_404(Product, slug=self.kwargs["slug"])
        return product.videos.all()


@staff_member_required
def get_filter_options(request):
    grouped_purchases = Purchase.objects.annotate(year=ExtractYear('time')).values('year').order_by('-year').distinct()
    options = [purchase['year'] for purchase in grouped_purchases]

    return JsonResponse({
        'options': options,
    })


@staff_member_required
def get_sales_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)
    grouped_purchases = purchases.annotate(aliexpress_price=F('product__aliexpress_price')).annotate(month=ExtractMonth('time'))\
        .values('month').annotate(average=Sum('product__aliexpress_price')).values('month', 'average').order_by('month')

    sales_dict = get_year_dict()

    for group in grouped_purchases:
        sales_dict[months[group['month']-1]] = round(group['average'], 2)

    return JsonResponse({
        'title': f'Sales in {year}',
        'data': {
            'labels': list(sales_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(sales_dict.values()),
            }]
        },
    })


@staff_member_required
def spend_per_customer_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)
    grouped_purchases = purchases.annotate(aliexpress_price=F('product__aliexpress_price')).annotate(month=ExtractMonth('time'))\
        .values('month').annotate(average=Avg('product__aliexpress_price')).values('month', 'average').order_by('month')

    spend_per_customer_dict = get_year_dict()

    for group in grouped_purchases:
        spend_per_customer_dict[months[group['month']-1]] = round(group['average'], 2)

    return JsonResponse({
        'title': f'Spend per customer in {year}',
        'data': {
            'labels': list(spend_per_customer_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(spend_per_customer_dict.values()),
            }]
        },
    })


@staff_member_required
def payment_success_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)

    return JsonResponse({
        'title': f'Payment success rate in {year}',
        'data': {
            'labels': ['Successful', 'Unsuccessful'],
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': [colorSuccess, colorDanger],
                'borderColor': [colorSuccess, colorDanger],
                'data': [
                    purchases.filter(successful=True).count(),
                    purchases.filter(successful=False).count(),
                ],
            }]
        },
    })


@staff_member_required
def payment_method_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)
    grouped_purchases = purchases.values('payment_method').annotate(count=Count('id'))\
        .values('payment_method', 'count').order_by('payment_method')

    payment_method_dict = dict()

    for payment_method in Purchase.PAYMENT_METHODS:
        payment_method_dict[payment_method[1]] = 0

    for group in grouped_purchases:
        payment_method_dict[dict(Purchase.PAYMENT_METHODS)[group['payment_method']]] = group['count']

    return JsonResponse({
        'title': f'Payment method rate in {year}',
        'data': {
            'labels': list(payment_method_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': generate_color_palette(len(payment_method_dict)),
                'borderColor': generate_color_palette(len(payment_method_dict)),
                'data': list(payment_method_dict.values()),
            }]
        },
    })