# Generated by Django 3.2 on 2022-09-08 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_suppliers_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_seen',
            field=models.DateTimeField(),
        ),
    ]