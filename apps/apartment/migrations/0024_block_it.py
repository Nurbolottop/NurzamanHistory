# Generated by Django 5.0 on 2023-12-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0023_block_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='it',
            field=models.IntegerField(default=1, verbose_name='Нумерация'),
        ),
    ]
