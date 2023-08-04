# Generated by Django 4.2.3 on 2023-08-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_promotion_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotion',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Акция'),
        ),
    ]
