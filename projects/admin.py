from typing import Any
from django.contrib import admin
from .models import Project
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class ProjectResources(resources.ModelResource):
    class Meta:
        model = Project
        fields = ['id','standard','exam','chapter','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']
        export_order = ['id','standard','exam','chapter','description','date_added','date_updated',
                  'uploaded_by__name','uploaded_by__phone_number','uploaded_by__email','file']


class ProjectAdmin(ImportExportModelAdmin):
    view_on_site = False
    fields=('standard','exam','chapter','description','file')
    list_display = ('standard','exam','chapter','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','exam','uploaded_by')
    search_fields =('standard','exam', 'chapter','uploaded_by__name')
    resource_class = ProjectResources
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Project,ProjectAdmin)

