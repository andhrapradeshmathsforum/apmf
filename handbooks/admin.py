from typing import Any
from django.contrib import admin
from .models import Handbook
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class HandbookResources(resources.ModelResource):
    class Meta:
        model = Handbook
        fields = ['id','standard','title','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']
        export_order = ['id','standard','title','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']
class HandbookAdmin(ImportExportModelAdmin):    
    view_on_site = False
    fields=('standard','title','description','file')    
    list_display = ('standard','title','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','uploaded_by')
    search_fields =('standard', 'title','uploaded_by__name')
    resouce_class = HandbookResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Handbook, HandbookAdmin)