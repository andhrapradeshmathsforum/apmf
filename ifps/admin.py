from django.contrib import admin
from .models import Ifp
from typing import Any
from embed_video.admin import AdminVideoMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class IfpResources(resources.ModelResource):
    class Meta:
        model = Ifp
        fields = ['id','title','description','date_added','date_updated','uploaded_by__name',
                  'uploaded_by__phone_number', 'uploaded_by__email','video']
        export_order =  ['id','title','description','date_added','date_updated','uploaded_by__name',
                  'uploaded_by__phone_number', 'uploaded_by__email','video']
class IfpAdmin(AdminVideoMixin, ImportExportModelAdmin):    
    view_on_site = False
    fields=('title','description','video')    
    list_display = ('title','date_added','date_updated','uploaded_by','video')
    list_filter = ('uploaded_by',)
    search_fields =('title', 'description','uploaded_by__name')
    resource_class = IfpResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Ifp, IfpAdmin)