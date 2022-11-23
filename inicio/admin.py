from django.contrib import admin
from .models import Compra
# Register your models here.

class ComprasAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

admin.site.register(Compra, ComprasAdmin)