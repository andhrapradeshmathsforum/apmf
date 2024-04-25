from typing import Any
from django.contrib import admin
from .models import News
from django.utils.html import format_html

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    fields = ('heading','body','image', 'attachment')   
    
    list_display =['heading','image','attachment','date_added','uploaded_by']
       
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(News, NewsAdmin)



