# Generated by Django 3.2 on 2022-09-13 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='age',
            name='name',
        ),
    ]