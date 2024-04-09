from django.contrib import admin
from .models import Notes
from typing import Any

# Register your models here.


class NotesnAdmin(admin.ModelAdmin):
    view_on_site = False
    fields=('standard','chapter','description','uploaded_by','file')
    list_display = ('standard','chapter','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','uploaded_by')
    search_fields =('standard','chapter', 'description','uploaded_by__name')
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Notes, NotesnAdmin)