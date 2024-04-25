from typing import Any
from django.contrib import admin
from .models import Hot
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class HotResources(resources.ModelResource):
    class Meta:
        model = Hot
        fields = ('id','standard','chapter','title','date_added',
                        'date_updated','uploaded_by__name','uploaded_by__phone_number',
                        'uploaded_by__email','file')
        export_order = ('id','standard','chapter','title','date_added',
                        'date_updated','uploaded_by__name','uploaded_by__phone_number',
                        'uploaded_by__email','file')
        

class HotModelAdmin(ImportExportModelAdmin):
    view_on_site = False
    fields = ('standard','chapter','title','file')
    list_display = ['id','standard','chapter','title','date_added','date_updated','uploaded_by','file']
    list_filter = ['standard','chapter','uploaded_by']
    search_fields = ['standard','chapter','title','description','uploaded_by__name']
    resource_class = HotResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Hot, HotModelAdmin)

