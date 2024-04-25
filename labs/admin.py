from typing import Any
from django.contrib import admin
from .models import Lab
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class LabResources(resources.ModelResource):
    class Meta:
        model = Lab
        fields = ['id','standard','title','description','uploaded_by__name',
                  'uploaded_by__phone_number','uploaded_by__email','file']
        export_order = ['id','standard','title','description','uploaded_by__name',
                  'uploaded_by__phone_number','uploaded_by__email','file']
class LabAdmin(ImportExportModelAdmin):    
    view_on_site = False
    fields=('standard','title','description','file')    
    list_display = ('standard','title','date_added','date_updated','uploaded_by','file')
    list_filter = ['standard','uploaded_by']
    search_fields =('standard','title','uploaded_by__name')
    resource_class = LabResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Lab, LabAdmin)