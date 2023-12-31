# Generated by Django 4.2.3 on 2023-07-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена')),
                ('description', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
