# Generated by Django 3.2 on 2022-11-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_aliexpress_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='aliexpress_total_sale',
            field=models.IntegerField(default=0, help_text='Amount of aliexpress sale generated'),
        ),
    ]
