from django.contrib import admin
from .models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    view_on_site = False
    fields=('standard','exam','chapter','description','uploaded_by','file')
    list_display = ('standard','exam','chapter','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','exam','uploaded_by')
    search_fields =('standard','exam', 'chapter','uploaded_by__name')
admin.site.register(Project,ProjectAdmin)

