from django.contrib import admin

# Register your models here.

from .models import File, LiquidCrystal, Polyimide, Seal, Vender
from .models import Adhesion
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