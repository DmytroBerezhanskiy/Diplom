# Generated by Django 3.1.7 on 2021-05-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_orderitem_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('received', 'Received'), ('order collection', 'Order collection'), ('delivery', 'Delivery'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], default='received', max_length=20),
        ),
    ]