# Generated by Django 5.0 on 2023-12-22 19:59

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contactinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='gallery/', verbose_name='Фотография'),
        ),
    ]