from typing import Any
from django.contrib import admin
from .models import Otherbook

# Register your models here.


class OtherbookAdmin(admin.ModelAdmin):    
    view_on_site = False
    fields=('title','description','uploaded_by','file')    
    list_display = ('title','date_added','date_updated','uploaded_by','file')
    list_filter = ['uploaded_by']
    search_fields =('title','uploaded_by__name')
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Otherbook, OtherbookAdmin)