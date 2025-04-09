from django.contrib import admin
from .models import Level, Workshop
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Level)
class LevelAdmin(SummernoteModelAdmin):

    list_display = ('name',)
    search_fields = ['name']
    list_filter = ('name',)


@admin.register(Workshop)
class WorkshopAdmin(SummernoteModelAdmin):

    list_display = ('name', 'is_public')
    search_fields = ['level']
    # list_filter = ('level',)
    summernote_fields = ('description',)
