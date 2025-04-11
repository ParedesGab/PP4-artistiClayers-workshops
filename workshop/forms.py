from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('workshop', 'participants', 'appointment_date',)
        widgets = {
            'appointment_date': forms.SplitDateTimeWidget(
                date_attrs={'type': 'date'},
                time_attrs={'type': 'time'}
                ),
        }
