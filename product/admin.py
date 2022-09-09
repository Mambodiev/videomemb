from django.contrib import admin

from .models import Pricing, Subscription, Category 
from . import models

@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Pricing)
admin.site.register(Category)
admin.site.register(Subscription)
