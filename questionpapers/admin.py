from django.contrib import admin
from .models import Questionpaper
from typing import Any


# Register your models here.


class QuestionpaperAdmin(admin.ModelAdmin):    
    view_on_site = False
    fields=('standard','exam','description','file')    
    list_display = ('standard','exam','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','exam','uploaded_by')
    search_fields =('standard','exam', 'description','uploaded_by__name')
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Questionpaper, QuestionpaperAdmin)