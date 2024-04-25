from typing import Any
from django.contrib import admin
from .models import Mindmap
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class MindmapResources(resources.ModelResource):
    class Meta:
        model = Mindmap
        fields = ('id','standard','chapter','title','date_added',
                        'date_updated','uploaded_by__name','uploaded_by__phone_number',
                        'uploaded_by__email','file')
        export_order = ('id','standard','chapter','title','date_added',
                        'date_updated','uploaded_by__name','uploaded_by__phone_number',
                        'uploaded_by__email','file')
        

class MindmapModelAdmin(ImportExportModelAdmin):
    view_on_site = False
    fields = ('standard','chapter','title','file')
    list_display = ['id','standard','chapter','title','date_added','date_updated','uploaded_by','file']
    list_filter = ['standard','chapter','uploaded_by']
    search_fields = ['standard','chapter','title','description','uploaded_by__name']
    resource_class = MindmapResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Mindmap, MindmapModelAdmin)

