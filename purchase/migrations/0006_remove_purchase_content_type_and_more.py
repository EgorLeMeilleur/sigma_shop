# Generated by Django 4.2.3 on 2023-07-29 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0005_purchase_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='object_id',
        ),
    ]
