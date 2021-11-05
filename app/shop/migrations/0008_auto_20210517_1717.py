# Generated by Django 3.1.7 on 2021-05-17 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_auto_20210516_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'default_related_name': 'category', 'ordering': ('name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1 - Very bad'), (2, '2 - Bad'), (3, '3 - Okay'), (4, '4 - Great'), (5, '5 - Excellent')], null=True),
        ),
        migrations.CreateModel(
            name='ReviewsAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='shop.reviews')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
