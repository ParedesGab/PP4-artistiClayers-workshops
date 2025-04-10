from django.contrib import admin
from .models import CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(SummernoteModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'read',)
    summernote_fields = ('message',)
