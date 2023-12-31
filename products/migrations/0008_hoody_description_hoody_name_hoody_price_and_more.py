# Generated by Django 4.2.3 on 2023-07-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_hoody_description_remove_hoody_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoody',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='hoody',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='hoody',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='sweatshirt',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='sweatshirt',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='sweatshirt',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена'),
        ),
    ]
