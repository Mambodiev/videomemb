# Generated by Django 3.2 on 2022-11-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_aliexpress_total_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_of_store_selling',
            field=models.IntegerField(default=0, help_text='Amount of store selling the product'),
        ),
    ]
