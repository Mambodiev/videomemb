# Generated by Django 3.2 on 2022-08-09 00:06

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20220808_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
