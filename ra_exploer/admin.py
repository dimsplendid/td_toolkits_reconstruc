from django.contrib import admin

# Register your models here.

from .models import LiquidCrystal, Polyimide, Seal, Vendor, TemplateItem, TemplateCond, VHR, DeltaAngle, Adhesion

admin.site.register(LiquidCrystal)
admin.site.register(Polyimide)
admin.site.register(Seal)
admin.site.register(Vendor)
# admin.site.register(TemplateItem)
admin.site.register(TemplateCond)
admin.site.register(VHR)
admin.site.register(DeltaAngle)
admin.site.register(Adhesion)


class TemplateItemAdmin(admin.ModelAdmin):
    list_display = ('LC', 'PI', 'seal', 'cond',
                    'value', 'file_source', 'vendor')


admin.site.register(TemplateItem, TemplateItemAdmin)
