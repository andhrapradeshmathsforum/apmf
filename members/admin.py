from typing import Any
from django.contrib import admin
from .models import Member

# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ['name','designation','phone_number','school','mandal','district','image','uploaded_by']
    fields = ['name','designation','phone_number','school','mandal','district','image']
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Member, MembersAdmin)