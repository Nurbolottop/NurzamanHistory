# Generated by Django 5.0 on 2023-12-22 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0012_alter_environment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enviromenttitle',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='environment_test', to='secondary.environment'),
        ),
    ]