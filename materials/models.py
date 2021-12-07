from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class LiquidCrystal(models.Model):
    """Model record LC"""
    name = models.CharField(max_length=20, unique=True,
                            help_text='Enter a LC name')
    vender = ForeignKey('ra_exploer.Vender', on_delete=models.RESTRICT,
                        null=True, blank=True)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class Polyimide(models.Model):
    """Model record PI"""
    name = models.CharField(max_length=20, unique=True,
                            help_text='Enter a PI name')

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class Seal(models.Model):
    """Model record Seal"""
    name = models.CharField(max_length=20, unique=True,
                            help_text='Enter a Seal name')

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name

