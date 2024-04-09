from django.contrib import admin
from .models import Solution

# Register your models here.


class SolutionAdmin(admin.ModelAdmin):    
    view_on_site = False
    fields=('standard','chapter','description','uploaded_by','file')    
    list_display = ('standard','chapter','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','uploaded_by')
    search_fields =('standard','chapter','uploaded_by__name')
admin.site.register(Solution, SolutionAdmin)