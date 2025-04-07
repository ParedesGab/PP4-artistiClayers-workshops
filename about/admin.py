from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title', )
    search_fields = ['title']
    list_filter = ('title',)
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

