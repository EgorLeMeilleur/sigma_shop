# Generated by Django 4.2.3 on 2023-07-29 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_remove_purchase_product_purchase_content_type_and_more'),
        ('wishes', '0002_remove_wishes_product_wishes_content_type_and_more'),
        ('products', '0002_hoody_sweatshirt_tshirt'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]