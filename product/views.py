from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Product
from .filters import ProductFilter


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