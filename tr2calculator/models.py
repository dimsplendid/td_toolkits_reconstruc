from django.db import models
from django.db.models.fields.related import ForeignKey

from materials.models import LiquidCrystal

# > python manage.py makemigrations
# > python manage.py migrate
# Warning: You'll need to run these commands every time
# your models change in a way that will affect the structure of
# the data that needs to be stored
# (including both addition and removal of whole models and individual fields).


# Create your models here.
class AxomatricsLog(models.Model):
    pass


class Condition(models.Model):
    pass


class Batch(models.Model):
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value


class Plateform(models.Model):
    abbr = models.CharField(max_length=5, default='5905')

    def __str__(self) -> str:
        return self.abbr


class OpticsLogTest(models.Model):
    batch = ForeignKey(Batch, on_delete=models.RESTRICT)
    liquidCrystal = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT)
    v90 = models.DecimalField(
        max_digits=5, decimal_places=4)
    v95 = models.DecimalField(
        max_digits=5, decimal_places=4)
    v99 = models.DecimalField(
        max_digits=5, decimal_places=4)
    v100 = models.DecimalField(
        max_digits=5, decimal_places=4)
    vop = models.DecimalField(
        max_digits=5, decimal_places=4)

    class VoltagePercent(models.TextChoices):
        V90 = 'V90', 'V90'
        V95 = 'V95', 'V95'
        V99 = 'V99', 'V99'
        V100 = 'V100', 'V100'
        VREF = 'Vref', 'Vref'

    v_percent = models.CharField(
        max_length=4,
        choices=VoltagePercent.choices,
    )
    platform = ForeignKey(Plateform, null=True, on_delete=models.SET_NULL)
    cell_gap = models.DecimalField(
        max_digits=3, decimal_places=2)
    lc_percent = models.DecimalField(
        max_digits=6, decimal_places=3)

    ref_record = ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)

    wx = models.DecimalField(
        max_digits=20, decimal_places=9)

    @property
    def wx_gain(self):
        return self.wx - self.ref_record.wx

    wy = models.DecimalField(
        max_digits=20, decimal_places=9)

    @property
    def wy_gain(self):
        return self.wx - self.ref_record.wx

    u_prime = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    v_prime = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    delta_uv = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    a_star = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    b_star = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    l_star = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    delta_a_star = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    delta_b_star = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    delta_l_star = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    delta_e_ab_star = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    contrast_ratio = models.DecimalField(
        max_digits=5,
        decimal_places=1,
    )

    delta_contrast_ratio = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    transmittance = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        null=True,
        blank=True,
    )

    @property
    def scatter(self):
        return self.cell_gap * self.liquidCrystal.scatter_index

    dark_index = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    white_index = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    time_rise = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    time_fall = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    response_time = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    g2g = models.DecimalField(
        max_digits=20,
        decimal_places=9,
    )

    class RemarkChoice(models.TextChoices):
        EXTRA = 'Extrapolation', 'Extrapolation'
        INTER = 'Interpolation', 'Interpolation'

    remark = models.CharField(
        max_length=20,
        choices=RemarkChoice.choices,
        default=RemarkChoice.EXTRA,
    )
