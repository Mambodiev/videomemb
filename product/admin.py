from django.contrib import admin

from .models import Age, Pricing, Subscription
from . import models

@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title',]
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Pricing)
admin.site.register(Subscription)
admin.site.register(Age)
