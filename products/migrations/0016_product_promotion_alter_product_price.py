# Generated by Django 4.2.3 on 2023-08-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_productimage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='promotion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Акция'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=8, null=True, verbose_name='Цена'),
        ),
    ]
