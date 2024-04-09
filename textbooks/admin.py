from django.contrib import admin
from .models import Textbook

# Register your models here.


class TextbookAdmin(admin.ModelAdmin):    
    view_on_site = False
    fields=('standard','semester','title','description','uploaded_by','file')    
    list_display = ('standard','semester','title','date_added','date_updated','uploaded_by','file')
    list_filter = ('standard','semester','uploaded_by')
    search_fields =('standard','semester', 'title','uploaded_by__name')
admin.site.register(Textbook, TextbookAdmin)