from django.contrib import admin

# Register your models here.
from .models import LiquidCrystal, Polyimide, Seal

admin.site.register(LiquidCrystal)
admin.site.register(Polyimide)
admin.site.register(Seal)