from django.contrib import admin

# Register your models here.

from .models import VHR, DeltaAngle, File, LowTemperatureStorage, Validator, Vender
from .models import (
    Adhesion, 
    LowTemperatureOperation, 
    PressureCookingTest, 
    SealWVTR,
    UShapeAC,
)
# from .models import VHR, DeltaAngle, Adhesion
# from .models import LowTemperatrueOperation, LowTemperatrueStorage, ACIS

admin.site.register(Vender)
admin.site.register(File)
# admin.site.register(VHR)
# admin.site.register(DeltaAngle)
# admin.site.register(Adhesion)
# admin.site.register(LowTemperatrueStorage)
# admin.site.register(LowTemperatrueOperation)
# admin.site.register(ACIS)


class TemplateItemAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'cond',
                    'value', 'file_source', 'vendor')

# class VHRAdmin(admin.ModelAdmin):
#     list_display = ('LC', 'PI', 'seal', 'measure_voltage',
#                     'measure_freq', 'value', 'vendor', 'file_source')

# admin.site.register(VHR, VHRAdmin)


class AdhesionAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(Adhesion, AdhesionAdmin)


class LTOAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(LowTemperatureOperation, LTOAdmin)


class LTSAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(LowTemperatureStorage, LTSAdmin)


class DeltaAngleAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(DeltaAngle, DeltaAngleAdmin)


class VHRAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(VHR, VHRAdmin)


class ValidatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


admin.site.register(Validator, ValidatorAdmin)



class PCTAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(PressureCookingTest, PCTAdmin)

class SealWVTRAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(SealWVTR, SealWVTRAdmin)

class UShapeACAdimin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')

admin.site.register(UShapeAC, UShapeACAdimin)