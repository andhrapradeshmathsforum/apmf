from django.contrib import admin
from .models import Teachingvideo
from typing import Any
from embed_video.admin import AdminVideoMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class TeachingvideoResources(resources.ModelResource):
    class Meta:
        model = Teachingvideo
        fields = ('id','standard','title','description','date_added','date_updated',
                  'uploaded_by__name', 'uploaded_by__phone_number','uploaded_by__email',
                  'video',)
        export_order = ('id','standard','title','description','date_added','date_updated',
                  'uploaded_by__name', 'uploaded_by__phone_number','uploaded_by__email',
                  'video')


class TeachingvideoAdmin(AdminVideoMixin, ImportExportModelAdmin):    
    view_on_site = False
    fields=('standard','title','description','video')    
    list_display = ('standard','title','date_added','date_updated','uploaded_by','video')
    list_filter = ['standard','uploaded_by']
    search_fields =('standard','title', 'description','uploaded_by__name')
    resource_class = TeachingvideoResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Teachingvideo, TeachingvideoAdmin)