from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('workshop', 'participants', 'appointment_date',)
        widgets = {
            'appointment_date': forms.widgets.DateTimeInput(
                attrs={
                        'type': 'datetime-local',
                        'required': 'required'
                    }
                )
        }
