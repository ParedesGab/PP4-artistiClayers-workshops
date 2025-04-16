from django.contrib import admin
from .models import Level, Workshop, Booking
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
    summernote_fields = ('description', 'excerpt')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("workshop", "booked_by", "appointment_date",
                    "participants", "date_booked",)
    search_fields = ("booked_by__username", "workshop__name")
    list_filter = ("workshop", "appointment_date")
