# Generated by Django 5.0 on 2024-01-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0030_osob_alter_apartmentosob_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osob',
            options={'verbose_name': 'Добавить Особенность', 'verbose_name_plural': 'Добавить Особенности'},
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]