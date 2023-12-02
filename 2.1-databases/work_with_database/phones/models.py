from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    image = models.URLField(max_length=300, default=None)
    price = models.PositiveIntegerField()
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(max_length=150, unique=True)
