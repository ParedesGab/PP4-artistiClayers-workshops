from django.contrib import admin
from .models import ContactRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactRequest)
class ContactRequestAdmin(SummernoteModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'read',)
    summernote_fields = ('message',)
