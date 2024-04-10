from typing import Any
from django.contrib import admin
from .models import Handbook

# Register your models here.


class HandbookAdmin(admin.ModelAdmin):    
    view_on_site = False
    fields=('standard','title','description','uploaded_by','file')    
    list_display = ('standard','title','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','uploaded_by')
    search_fields =('standard', 'title','uploaded_by__name')
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Handbook, HandbookAdmin)