from django.contrib import admin

from .models import Request, RequestMessage


class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created']
    search_fields = ['title']

class RequestMessageAdmin(admin.ModelAdmin):
    list_display = ['requestapp', 'text', 'created']
    search_fields = ['text']

admin.site.register(Request, RequestAdmin)
admin.site.register(RequestMessage, RequestMessageAdmin)
