# Generated by Django 5.0 on 2023-12-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0006_category_apartment_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('price_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('price_max', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('size_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('size_max', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('floor_min', models.IntegerField(blank=True, null=True)),
                ('floor_max', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
