# Generated by Django 3.2 on 2022-09-12 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220912_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='language_the_ads',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='social_media_name',
            new_name='media_type',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_cost',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ads_type',
            new_name='site_type',
        ),
    ]
