from typing import Any
from django.contrib import admin
from .models import Otherbook
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class OtherbookResources(resources.ModelResource):
    class Meta:
        model = Otherbook
        fields = ['id','title','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']

class OtherbookAdmin(ImportExportModelAdmin):    
    view_on_site = False
    fields=('title','description','file')    
    list_display = ('title','date_added','date_updated','uploaded_by','file')
    list_filter = ['uploaded_by']
    search_fields =('title','uploaded_by__name')
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Otherbook, OtherbookAdmin)