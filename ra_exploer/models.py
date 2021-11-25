from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


# Create your models here.


class LiquidCrystal(models.Model):
    """Model record LC"""
    name = models.CharField(max_length=20, unique=True,
                            help_text='Enter a LC name')
    vender = ForeignKey('Vender', on_delete=models.RESTRICT, null=True, blank=True)

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


class Vender(models.Model):
    """Model record Vender"""
    name = models.CharField(max_length=200, unique=True,
                            help_text="Vender name")

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            help_text='Input file name')

    def __str__(self):
        return self.name


class Validator(models.Model):
    # date = models.DateField()
    name = models.CharField(
        max_length=20,
        default='FOO',
        unique=True,
    )
    value = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        default=0.00,
    )

    def __str__(self):
        return str(self.value)

def valid_id_map(name):
    items = {
        'VHR(heat)': 1,
    }
    return items[name]
 
class VHR(models.Model):
    name = 'VHR(heat)'
    LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
                    null=True, blank=True)
    PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
                    null=True, blank=True)
    seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

    BeforeUV = 'Before UV'
    AfterUV = 'After UV'
    UV_aging = models.CharField(
        max_length=10,
        choices=(
            (BeforeUV, 'Before UV'),
            (AfterUV, 'After UV')
        ),
        default='Before UV'
    )

    measure_voltage = models.DecimalField(
        max_digits=5, decimal_places=2, default=1.0)
    measure_freq = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.6)
    measure_temperature = models.DecimalField(
        max_digits=5, decimal_places=2, default=60)
    value = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    unit = '%'
    vender = ForeignKey(Vender, on_delete=models.RESTRICT, null=True)
    file_source = ForeignKey(File, on_delete=models.RESTRICT)

    valid_value = ForeignKey(Validator, on_delete=models.RESTRICT, default=valid_id_map(name))
    
    def cond(self):
        return self.UV_aging + ', V: ' + str(self.measure_voltage) + ' volt, freq: ' + str(
            self.measure_freq) + ' Hz, Temperature: ' + str(self.measure_temperature) + ' °C'

    def value_remark(self):
        return ''


class DeltaAngle(models.Model):
    name = 'Δ angle'
    LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
                    null=True, blank=True)
    PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
                    null=True, blank=True)
    seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)
    measure_voltage = models.DecimalField(
        max_digits=5, decimal_places=2, default=14.0)
    measure_freq = models.DecimalField(
        max_digits=5, decimal_places=2, default=60.0)
    measure_time = models.DecimalField(
        max_digits=5, decimal_places=2, default=72.0)
    measure_temperature = models.DecimalField(
        max_digits=5, decimal_places=2, default=60.0, null=True)
    value = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    vender = ForeignKey(Vender, on_delete=models.RESTRICT, null=True)
    unit = '°'
    file_source = ForeignKey(File, on_delete=models.RESTRICT)

    def cond(self):
        return str(self.measure_time) + ' hr, Vp-p: ' + str(self.measure_voltage) + ' volt, freq: ' + str(
            self.measure_freq) + ' Hz, Temperature: ' + str(self.measure_temperature) + ' °C'

    def value_remark(self):
        return ''


class Adhesion(models.Model):
    name = 'adhesion test'
    LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
                    null=True, blank=True)
    PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
                    null=True, blank=True)
    seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

    adhesion_interface = models.CharField(
        max_length=40, help_text='enter condition')
    method = models.CharField(max_length=200)

    value = models.DecimalField(max_digits=5, decimal_places=2)
    unit = 'kgw'

    peeling = models.CharField(
        max_length=40, help_text="Enter peeling interface.", blank=True, null=True)
    vender = ForeignKey(Vender, on_delete=models.RESTRICT)
    file_source = ForeignKey(File, on_delete=models.RESTRICT)

    def cond(self):
        return 'Adhesion介面(T/C): ' + str(self.adhesion_interface) + '測試手法' + str(self.method)

    def value_remark(self):
        return 'Peeling surface: ' + str(self.peeling)


class LowTemperatureStorage(models.Model):
    name = 'LTS'
    LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
                    null=True, blank=True)
    PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
                    null=True, blank=True)
    seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

    storage_condition = models.CharField(
        max_length=10,
        choices=(
            ('Bulk', 'Bulk'),
            ('Test Cell', 'Test Cell')
        )
    )

    SLV_condition = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    JarTestSeal = ForeignKey(
        Seal, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    measure_temperature = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    value = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    unit = 'days'
    vender = ForeignKey(Vender, on_delete=models.RESTRICT)

    file_source = ForeignKey(File, on_delete=models.RESTRICT)

    def cond(self):
        return str(self.measure_temperature) + ' °C, Storage: ' + self.storage_condition + ', SLV%: ' + str(
            float(self.SLV_condition or 0) * 100.) + '% , Jar test seal: ' + str(self.JarTestSeal)

    def value_remark(self):
        return ''


class LowTemperatureOperation(models.Model):
    name = 'LTO'
    LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
                    null=True, blank=True)
    PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
                    null=True, blank=True)
    seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

    storage_condition = models.CharField(
        max_length=10,
        default='Test Cell',
    )

    SLV_condition = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    JarTestSeal = ForeignKey(
        Seal, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    measure_temperature = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    class Value(models.IntegerChoices):
        NA = -1, "N.A."    
        NG = 0, "NG"
        PASS = 1, "Pass"

    value_mapping = {i.label: i.value for i in Value}
    value = models.IntegerField(
        choices=Value.choices,
        null=True,
    )
    unit = ''
    vender = ForeignKey(Vender, on_delete=models.RESTRICT, null=True)

    file_source = ForeignKey(File, on_delete=models.RESTRICT)

    def cond(self):
        return str(self.measure_temperature) + ' °C, Storage: ' + str(self.storage_condition) + ', SLV%: ' + str(
            float(self.SLV_condition or 0) * 100.)  + '% , Jar test seal: ' + str(self.JarTestSeal)

    def value_remark(self):
        return ''

# class ACIS(models.Model):
#     name = 'AC IS'
#     LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

#     device = CharField(max_length=20, null=True,
#                        blank=True, default='2211 Test Cell')
#     value = models.DecimalField(max_digits=4, decimal_places=2, null=True)
#     unit = '%'
#     vender = ForeignKey(Vender, on_delete=models.RESTRICT, null=True)

#     file_source = models.CharField(max_length=200, help_text="file name")

#     def cond(self):
#         return 'device: ' + str(self.device)

#     def value_remark(self):
#         return ''
