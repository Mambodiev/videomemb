from django.contrib import admin

from .models import Age, Pricing, Subscription, Gender, Country, Order
from . import models

@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title',]
    prepopulated_fields = {'slug': ('title',), }


class GenderAdmin(admin.ModelAdmin):
    list_display = ['name',]


class AgeAdmin(admin.ModelAdmin):
    list_display = ['name',]


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name',]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name',]


admin.site.register(Pricing)
admin.site.register(Subscription)
admin.site.register(Age)
admin.site.register(Gender)
admin.site.register(Country)
admin.site.register(Order)