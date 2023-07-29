# Generated by Django 4.2.3 on 2023-07-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hoody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='Описание')),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Худи',
            },
        ),
        migrations.CreateModel(
            name='Sweatshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='Описание')),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Свитшот',
                'verbose_name_plural': 'Свитшоты',
            },
        ),
        migrations.CreateModel(
            name='TShirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='Описание')),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Футболка',
                'verbose_name_plural': 'Футболки',
            },
        ),
    ]