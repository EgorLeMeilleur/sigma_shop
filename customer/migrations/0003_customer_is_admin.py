# Generated by Django 4.2.3 on 2023-07-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_options_customer_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_admin',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Админ'),
        ),
    ]
