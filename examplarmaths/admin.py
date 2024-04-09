from django.contrib import admin
from .models import Examplarmath

# Register your models here.


class ExamplarmathAdmin(admin.ModelAdmin):    
    view_on_site = False
    fields=('standard','title','description','uploaded_by','file')    
    list_display = ('standard','title','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','uploaded_by')
    search_fields =('standard', 'title','uploaded_by__name')
admin.site.register(Examplarmath, ExamplarmathAdmin)