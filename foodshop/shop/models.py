from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Shop(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        default_related_name = "shop"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        default_related_name = "category"

    def __str__(self):
        return self.name


class ProductQuerySet(models.query.QuerySet):

    def available(self):
        return self.filter(available=True)


class ProductManager(models.Manager):

    def get_query_set(self):
        return ProductQuerySet(self.model)

    def available(self):
        return self.get_query_set().available()


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    image = models.ImageField(upload_to='image_products/%Y/%d/%m', default='image_products/no_img.png')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        default_related_name = "products"

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])

    def get_shop_slug(self):
        shop = Shop.objects.get(name=self.shop)
        shop = shop.slug
        return reverse('product_list_by_shop',
                       args=[shop])

    def __str__(self):
        return self.name
