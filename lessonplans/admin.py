from typing import Any
from django.contrib import admin
from .models import Lessonplan
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class LessonplanResources(resources.ModelResource):
    class Meta:
        model = Lessonplan
        fields = ['id','standard','chapter','description','uploaded_by__name',
                  'uploaded_by__phone_number','uploaded_by__email','file']
        export_order = ['id','standard','chapter','description','uploaded_by__name',
                  'uploaded_by__phone_number','uploaded_by__email','file']
class LessonplanAdmin(ImportExportModelAdmin):
    view_on_site = False
    fields=('standard','chapter','description','file')
    list_display = ('standard','chapter','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','uploaded_by')
    search_fields =('standard','chapter', 'description','uploaded_by__name')
    resource_class = LessonplanResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Lessonplan, LessonplanAdmin)