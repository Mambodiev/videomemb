from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Product, Sale
from .filters import ProductFilter

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse
from django.shortcuts import render

from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict

from django.http import JsonResponse



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


def sale_chart(request):
    labels = []
    data = []

    queryset = Sale.objects.values()
    for entry in queryset:
        labels.append(entry['month_name'])
        data.append(entry['total_number_of_sale'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

class VideoDetailView(generic.DetailView):
    template_name = "product/video_detail.html"

    # def get_object(self):
    #     video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
    #     return video

    def get_queryset(self):
        product = get_object_or_404(Product, slug=self.kwargs["slug"])
        return product.videos.all()
