from django.contrib import admin
from .models import Ifp
from typing import Any
from embed_video.admin import AdminVideoMixin

# Register your models here.


class IfpAdmin(AdminVideoMixin, admin.ModelAdmin):    
    view_on_site = False
    fields=('title','description','video')    
    list_display = ('title','date_added','date_updated','uploaded_by','video')
    list_filter = ('uploaded_by',)
    search_fields =('title', 'description','uploaded_by__name')
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Ifp, IfpAdmin)