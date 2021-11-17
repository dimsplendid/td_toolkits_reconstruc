from django.contrib import admin

# Register your models here.

from .models import VHR, DeltaAngle, File, LiquidCrystal, LowTemperatrueStorage, Polyimide, Seal, Vender
from .models import Adhesion, LowTemperatrueOperation
# from .models import VHR, DeltaAngle, Adhesion
# from .models import LowTemperatrueOperation, LowTemperatrueStorage, ACIS

admin.site.register(LiquidCrystal)
admin.site.register(Polyimide)
admin.site.register(Seal)
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


admin.site.register(LowTemperatrueOperation, LTOAdmin)


class LTSAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(LowTemperatrueStorage, LTSAdmin)


class DeltaAngleAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(DeltaAngle, DeltaAngleAdmin)


class VHRAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'value')


admin.site.register(VHR, VHRAdmin)
