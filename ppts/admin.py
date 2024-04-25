from typing import Any
from django.contrib import admin
from .models import Ppt
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PptResources(resources.ModelResource):
    class Meta:
        model = Ppt
        fields = ['id','standard','chapter','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']
        export_order = ['id','standard','chapter','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']

class PptAdmin(ImportExportModelAdmin):    
    view_on_site = False
    fields=('standard','chapter','description','file')    
    list_display = ('standard','chapter','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','uploaded_by')
    search_fields =('standard','chapter', 'uploaded_by__name')
    resource_class = PptResources

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Ppt, PptAdmin)