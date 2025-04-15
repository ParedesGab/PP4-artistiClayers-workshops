from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = "date"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'workshop', 'participants',
            'appointment_date', 'appointment_time'
        )
        widgets = {
            'appointment_date': DateInput()
        }
