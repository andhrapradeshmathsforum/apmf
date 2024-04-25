from django.contrib import admin
from .models import Ict
from typing import Any
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class IctResources(resources.ModelResource):
    class Meta:
        model = Ict
        fields = ['id','title','link','date_added','date_updated','uploaded_by__name',
                  'uploaded_by__phone_number','uploaded_by__email','image']
        export_order = ['id','title','link','date_added','date_updated','uploaded_by__name',
                  'uploaded_by__phone_number','uploaded_by__email','image']

class IctAdmin(ImportExportModelAdmin):    
    view_on_site = False
    fields=('title','link','image')    
    list_display = ('title','link','date_added','date_updated','uploaded_by','image')
    list_filter = ['uploaded_by']
    search_fields =('title','link', 'uploaded_by__name')
    resource_class = IctResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Ict, IctAdmin)