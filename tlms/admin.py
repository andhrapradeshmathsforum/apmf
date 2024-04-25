from typing import Any
from django.contrib import admin
from .models import Tlm
from imagekit.admin import AdminThumbnail
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class TlmResources(resources.ModelResource):
    class Meta:
        model = Tlm
        fields = ('id','title', 'description', 'date_added','date_updated','image','uploaded_by__name','uploaded_by__email','uploaded_by__phone_number',)
        export_order = ('id','title', 'description', 'date_added','date_updated','image','uploaded_by__name','uploaded_by__email','uploaded_by__phone_number')

class Tlmadmin(ImportExportModelAdmin):
    fields = ['title','description','image']
    admin_thumbnail = AdminThumbnail(image_field='image_thumbnail')
    list_display =['title','description', 'date_added','admin_thumbnail', 'uploaded_by']    
    search_fields = ['title','description','uploaded_by.name']
    list_filter=['uploaded_by']
    resource_class = TlmResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
    
admin.site.register(Tlm, Tlmadmin)
