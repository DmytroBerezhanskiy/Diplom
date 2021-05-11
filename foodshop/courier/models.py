from django.db import models


class Courier(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=12)

    class Meta:
        ordering = ('surname', 'name')
        default_related_name = "courier"

    def __str__(self):
        return self.surname + " " + self.name
