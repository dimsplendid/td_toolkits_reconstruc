from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class LiquidCrystal(models.Model):
    """Model record LC"""
    name = models.CharField(max_length=20, help_text='Enter a LC name')

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class Polyimide(models.Model):
    """Model record PI"""
    name = models.CharField(max_length=20, help_text='Enter a PI name')

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class Seal(models.Model):
    """Model record Seal"""
    name = models.CharField(max_length=20, help_text='Enter a Seal name')

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class Vender(models.Model):
    """Model record Vender"""
    name = models.CharField(max_length=200, help_text="Vender name")

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=200, help_text='Input file name')
    def __str__(self):
        return self.name

# class VHR(models.Model):
#     name = 'VHR(heat)'
#     LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

#     BeforeUV = 'Before UV'
#     AfterUV = 'After UV'
#     condition = models.CharField(
#         max_length=10,
#         choices=(
#             (BeforeUV, 'Before UV'),
#             (AfterUV, 'After UV')
#         ),
#         default='Before UV'
#     )

#     measure_voltage = models.DecimalField(
#         max_digits=5, decimal_places=2, default=1.0)
#     measure_freq = models.DecimalField(
#         max_digits=5, decimal_places=2, default=0.6)
#     value = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#     unit = '%'
#     vender = ForeignKey(Vender, on_delete=models.RESTRICT, null=True)
#     file_source = models.CharField(max_length=200, help_text="file name")

#     def cond(self):
#         return self.condition + ', V: ' + str(self.measure_voltage) + ' volt, freq: ' + str(self.measure_freq) + ' Hz'

#     def value_remark(self):
#         return ''


# class DeltaAngle(models.Model):
#     name = 'Δangle'
#     LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)
#     measure_voltage = models.DecimalField(
#         max_digits=5, decimal_places=2, default=14.0)
#     measure_freq = models.DecimalField(
#         max_digits=5, decimal_places=2, default=60.0)
#     measure_time = models.DecimalField(
#         max_digits=5, decimal_places=2, default=72.0)
#     value = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#     vender = ForeignKey(Vender, on_delete=models.RESTRICT, null=True)
#     unit = '°'
#     file_source = models.CharField(max_length=200, help_text="file name")

#     def cond(self):
#         return str(self.measure_time) + ' hr, Vp-p: ' + str(self.measure_voltage) + ' volt, freq: ' + str(self.measure_freq) + ' Hz'

#     def value_remark(self):
#         return ''


class Adhesion(models.Model):
    name = 'adhesion test'
    LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
                    null=True, blank=True)
    PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
                    null=True, blank=True)
    seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

    adhesion_interface = models.CharField(max_length=40, help_text='enter condition')
    method = models.CharField(max_length=200)

    value = models.DecimalField(max_digits=5, decimal_places=2)
    unit = 'kgw'
    
    peeling = models.CharField(
        max_length=40, help_text="Enter peeling interface.", blank=True, null=True)
    vender = ForeignKey(Vender, on_delete=models.RESTRICT)
    file_source = ForeignKey(File, on_delete=models.RESTRICT)

    def cond(self):
        return self.condition

    def value_remark(self):
        return 'Adhesion介面(T/C): ' + str(self.adhesion_interface) + '測試手法' + str(self.method) + 'Peeling surface: ' + str(self.peeling)


# class LowTemperatrueStorage(models.Model):
#     name = 'LTS'
#     LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

#     storage_condtion = models.CharField(
#         max_length=10,
#         choices=(
#             ('Bulk', 'Bulk'),
#             ('Test Cell', 'Test Cell')
#         )
#     )

#     SLV_condtion = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True)
#     JarTestSeal = ForeignKey(
#         Seal, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
#     measure_temperature = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True)

#     value = models.DecimalField(max_digits=3, decimal_places=1, null=True)
#     unit = 'days'
#     vender = ForeignKey(Vender, on_delete=models.RESTRICT, null=True)

#     file_source = models.CharField(max_length=200, help_text="file name")

#     def cond(self):
#         return str(self.measure_temperature) + ' °C, Storage: ' + self.storage_condtion + ', SLV%: ' + str(self.SLV_condtion) + '% , Jar test seal: ' + str(self.JarTestSeal)

#     def value_remark(self):
#         return ''


# class LowTemperatrueOperation(models.Model):
#     name = 'LTO'
#     LC = ForeignKey(LiquidCrystal, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     PI = ForeignKey(Polyimide, on_delete=models.RESTRICT,
#                     null=True, blank=True)
#     seal = ForeignKey(Seal, on_delete=models.RESTRICT, null=True, blank=True)

#     storage_condtion = models.CharField(
#         max_length=10,
#         default='Test Cell',
#     )

#     SLV_condtion = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True)
#     JarTestSeal = ForeignKey(
#         Seal, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
#     measure_temperature = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True)

#     value = models.CharField(
#         max_length=10,
#         choices=(
#             ('OK', 'OK'),
#             ('NG', 'NG')
#         ),
#         null=True,
#     )
#     unit = ''
#     vender = ForeignKey(Vender, on_delete=models.RESTRICT, null=True)

#     file_source = models.CharField(max_length=200, help_text="file name")

#     def cond(self):
#         return str(self.measure_temperature) + ' °C, Storage: ' + self.storage_condtion + ', SLV%: ' + str(self.SLV_condtion) + '% , Jar test seal: ' + str(self.JarTestSeal)

#     def value_remark(self):
#         return ''


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
