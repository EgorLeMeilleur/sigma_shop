# Generated by Django 4.2.3 on 2023-07-29 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0008_alter_wishes_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wishes',
            unique_together=set(),
        ),
    ]
