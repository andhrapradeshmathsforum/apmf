from django.contrib import admin
from .models import Worksheet
from typing import Any
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class WorksheetResource(resources.ModelResource):
    class Meta:
        model = Worksheet
        fields = ('id', 'standard', 'chapter','description','date_added','date_updated','uploaded_by__name', 'uploaded_by__email','uploaded_by__phone_number',)
        export_order = ('id', 'standard', 'chapter','description','date_added','date_updated','uploaded_by__name', 'uploaded_by__email','uploaded_by__phone_number')

class WorksheetAdmin(ImportExportModelAdmin):    
    view_on_site = False
    fields=('standard','chapter','description','file')    
    list_display = ('standard','chapter','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','uploaded_by')
    search_fields =('standard','chapter', 'uploaded_by__name')
    resource_class = WorksheetResource
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Worksheet, WorksheetAdmin)