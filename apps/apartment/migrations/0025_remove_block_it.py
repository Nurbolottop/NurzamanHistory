# Generated by Django 5.0 on 2023-12-30 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0024_block_it'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='it',
        ),
    ]