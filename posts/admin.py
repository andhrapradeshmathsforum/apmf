from django.contrib import admin
from .models import Post
from typing import Any

# Register your models here.

class PostAdmin(admin.ModelAdmin):    
    view_on_site = False
    fields=('post',)    
    list_display = ('post','date_added','date_updated','uploaded_by')
    list_filter = ('uploaded_by',)
    search_fields =('post', 'uploaded_by__name')
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Post, PostAdmin)