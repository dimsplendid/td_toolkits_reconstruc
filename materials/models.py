from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class LiquidCrystal(models.Model):
    """Model record LC"""
    name = models.CharField(max_length=20, unique=True,
                            help_text='Enter a LC name')
    vender = ForeignKey('ra_exploer.Vender', on_delete=models.RESTRICT,
                        null=True, blank=True)

    n_e = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        null=True,
        blank=True,
    )

    n_o = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        null=True,
        blank=True,
    )

    @property
    def delta_n(self):
        return self.n_e - self.n_o

    scatter_index = models.DecimalField(
        max_digits=10,
        decimal_places=9,
        null=True,
        blank=True,
    )

    class Phases(models.TextChoices):
        TR1 = 'TR 1', 'TR 1'
        TR2 = 'TR 2', 'TR 2'
        TR3 = 'TR 3', 'TR 3'
        TR3H = 'TR 3.5', 'TR 3.5'

    phase = models.CharField(
        max_length=10,
        choices=Phases.choices,
        default=Phases.TR2,
        null=True,
        blank=True,
    )

    designed_cell_gap = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        default=3.0
    )

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
