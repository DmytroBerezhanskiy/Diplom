from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Promocode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    actual_from = models.DateTimeField()
    actual_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

