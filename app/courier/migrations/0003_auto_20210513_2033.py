# Generated by Django 3.1.7 on 2021-05-13 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0002_couriersreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couriersreview',
            name='order',
            field=models.CharField(max_length=100),
        ),
    ]