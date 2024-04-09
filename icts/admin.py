from django.contrib import admin
from .models import Ict
from typing import Any

# Register your models here.


class IctAdmin(admin.ModelAdmin):    
    view_on_site = False
    fields=('title','link','uploaded_by','image')    
    list_display = ('title','link','date_added','date_updated','uploaded_by','image')
    list_filter = ['uploaded_by']
    search_fields =('title','link', 'uploaded_by__name')
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Ict, IctAdmin)