from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(ModelPasangan)
class ItemAdmin(admin.ModelAdmin):
    exclude=("idsiasn ",)
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['idsiasn']
        else:
            return []
        
admin.site.register(ModelRwgolongan)
admin.site.register(Datautama)
admin.site.register(ModelRwPendidikan)
