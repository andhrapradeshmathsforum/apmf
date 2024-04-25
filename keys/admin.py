from typing import Any
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Key
from import_export import resources

# Register your models here.
class Keyresources(resources.ModelResource):
    class Meta:
        model = Key
        fields = ('standard','exam','year','title','description','date_added','date_updated',
              'uploaded_by__name','uploaded_by__phone_number','uploaded_by','file',)
        export_order = ('standard','exam','year','title','description','date_added','date_updated',
              'uploaded_by__name','uploaded_by__phone_number','uploaded_by','file')

class KeyAdmin(ImportExportModelAdmin):
    view_on_site = False
    fields = ('standard','exam','year','title','description','file')
    list_display = ('standard','exam','year','title','description','date_added','date_updated',
              'uploaded_by','file')
    list_filter = ('standard','exam','year','uploaded_by',)
    search_fields = ('standard','exam','year','uploaded_by',)
    resource_class = Keyresources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
    
admin.site.register(Key, KeyAdmin)