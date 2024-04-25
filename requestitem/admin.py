from django.contrib import admin
from . models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    view_on_site = False
    fields = ['request_for','message','name','phone_number']
    list_display = ['request_for','message','name','phone_number','date_added']
    list_filter = ['request_for']

admin.site.register(Message, MessageAdmin)
