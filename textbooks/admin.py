from typing import Any
from django.contrib import admin
from .models import Textbook
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
class TextbookResource(resources.ModelResource):

    class Meta:
        model = Textbook
        fields = ('id', 'standard', 'semester','title','description','date_added','date_updated','uploaded_by__name', 'uploaded_by__email','uploaded_by__phone_number', 'file')
        export_order = ('id', 'standard', 'semester','title','description','date_added','date_updated','uploaded_by__name', 'uploaded_by__email','uploaded_by__phone_number','file')


class TextbookAdmin(ImportExportModelAdmin):    
    view_on_site = False
    fields=('standard','semester','title','description','file')    
    list_display = ('standard','semester','title','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','semester','uploaded_by')
    search_fields =('standard','semester', 'title','uploaded_by__name')
    resource_class = TextbookResource
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Textbook, TextbookAdmin)