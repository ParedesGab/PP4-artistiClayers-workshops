from django.contrib import admin
from .models import Level, Workshop, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Level)
class LevelAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Level model,
    providing basic listing, searching, and filtering.
    """

    list_display = ('name',)
    search_fields = ['name']
    list_filter = ('name',)


@admin.register(Workshop)
class WorkshopAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Workshop model,
    enabling Summernote fields and providing listing, searching.
    """

    list_display = ('name', 'is_public')
    search_fields = ['level']
    summernote_fields = ('description', 'excerpt')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model,
    providing detailed listing, searching, and filtering.
    """
    list_display = ("id", "workshop", "booked_by", "appointment_date",
                    "participants", "date_booked",)
    search_fields = ("booked_by__username", "workshop__name")
    list_filter = ("workshop", "appointment_date")
