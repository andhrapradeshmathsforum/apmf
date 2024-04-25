from django.contrib import admin
from .models import Rp
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class RpResources(resources.ModelResource):
    class Meta:
        model = Rp
        fields = ['id','name','gender','phone_number','email','school','village','mandal','district',
                  'field','others','image']
        export_order = ['id','name','gender','phone_number','email','school','village','mandal','district',
                  'field','others','image']
        
class RpModelAdmin(ImportExportModelAdmin):
    view_on_site = False
    fields = ['name','gender','phone_number','email','school','village','mandal','district',
                  'field','others','image']
    list_display = ['name','gender','phone_number','email','school','village','mandal','district',
                  'field','others','image']
    list_filter = ['gender','district','field']
    resource_class = RpResources

admin.site.register(Rp, RpModelAdmin)

