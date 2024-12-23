from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.CharField(max_length=80, null=False)
    price = models.FloatField(null=False)
    image = models.CharField(max_length=200, null=False)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField(null=False)
    slug = AutoSlugField(populate_from='name', max_length=100,
                            unique=True, null=False)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.release_date}, {self.lte_exists}, {self.slug}, {self.image}'