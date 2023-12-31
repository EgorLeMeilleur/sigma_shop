# Generated by Django 4.2.3 on 2023-07-29 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishes',
            name='product',
        ),
        migrations.AddField(
            model_name='wishes',
            name='content_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='wishes',
            name='object_id',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
