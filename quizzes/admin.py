from typing import Any
from django.contrib import admin
from .models import Quiz
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.utils.html import format_html

# Register your models here.
class QuizResource(resources.ModelResource):

    class Meta:
        model = Quiz
        fields = ['id', 'standard', 'topic','sub_topic','link','date_added','date_updated','uploaded_by__name', 'uploaded_by__email','uploaded_by__phone_number']
        export_order = ['id', 'standard', 'topic','sub_topic','link','date_added','date_updated','uploaded_by__name', 'uploaded_by__email','uploaded_by__phone_number']

class QuizAdmin(ImportExportModelAdmin):    
    view_on_site = False    
    fields=('standard','topic','sub_topic','link')    
    list_display = ('standard','topic','sub_topic','date_added','date_updated','uploaded_by','link')
    
    list_filter = ('standard','topic','uploaded_by')
    search_fields =('standard','topic', 'sub_topic','uploaded_by__name')
    resource_class = QuizResource
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Quiz, QuizAdmin)

