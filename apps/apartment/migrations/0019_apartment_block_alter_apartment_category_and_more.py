# Generated by Django 5.0 on 2023-12-29 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0018_block_apartment_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='block_room', to='apartment.block', verbose_name='Выбрать блок'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_room', to='apartment.category', verbose_name='Выбрерите категорию'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartment',
            name='floor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='floor_form', to='apartment.floor', verbose_name='Сколько этаж'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartment',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.rooms', verbose_name='Выбрерите сколько комнат'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choise_room', to='apartment.status', verbose_name='Выбрерите статус'),
            preserve_default=False,
        ),
    ]