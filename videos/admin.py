from django.contrib import admin
from .models import Video
from typing import Any
from embed_video.admin import AdminVideoMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class VideoResource(resources.ModelResource):
    class Meta:
        model = Video
        fields = ('id', 'title', 'description','video','date_added','date_updated','uploaded_by__name', 'uploaded_by__email','uploaded_by__phone_number',)
        export_order = ('id', 'title', 'description','video','date_added','date_updated','uploaded_by__name', 'uploaded_by__email','uploaded_by__phone_number',)



class VideoAdmin(AdminVideoMixin, ImportExportModelAdmin):    
    view_on_site = False
    fields=('title','description','video')    
    list_display = ('title','date_added','date_updated','uploaded_by','video')
    list_filter = ('uploaded_by',)
    search_fields =('title', 'description','uploaded_by__name')
    resource_class = VideoResource
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Video, VideoAdmin)