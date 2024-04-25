from django.contrib import admin
from .models import Questionpaper
from typing import Any
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class QuestionpaperResource(resources.ModelResource):
    class Meta:
        model = Questionpaper
        fields = ['id','standard','exam','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']
        export_order = ['id','standard','exam','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']


class QuestionpaperAdmin(ImportExportModelAdmin):    
    view_on_site = False
    fields=('standard','exam','description','file')    
    list_display = ('standard','exam','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','exam','uploaded_by')
    search_fields =('standard','exam', 'description','uploaded_by__name')
    resource_class = QuestionpaperResource
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Questionpaper, QuestionpaperAdmin)