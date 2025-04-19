from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model,
    enabling Summernote on the description field.
    """
    summernote_fields = ('description',)
