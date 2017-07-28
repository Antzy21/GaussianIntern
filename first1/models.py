from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class Sankey(models.Model):
    target = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.source} -> {self.target}'


class Sankey2(models.Model):
    target = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    value = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.source} -> {self.target} = {self.value}'


class Pie1(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, validators=[MaxValueValidator(limit_value=100)])

    def __str__(self):
        return f'{self.name} = {self.value}'
