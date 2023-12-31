# Generated by Django 4.2.3 on 2023-07-29 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_sweatshirt_clothes_ptr_and_more'),
        ('wishes', '0005_remove_wishes_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishes',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_wish', to='products.product'),
        ),
    ]
