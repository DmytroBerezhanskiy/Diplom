# Generated by Django 3.1.7 on 2021-05-17 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210517_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ('created',), 'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
