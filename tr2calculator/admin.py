from django.contrib import admin

from .models import OpticsLogTest
# Register your models here.


class OpticsLogTestAdmin(admin.ModelAdmin):
    list_display = ('liquidCrystal', 'vop', 'v_percent', 'cell_gap')


admin.site.register(OpticsLogTest, OpticsLogTestAdmin)
