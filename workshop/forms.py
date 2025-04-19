from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    A custom form widget for displaying a date input field
    using the HTML5 'date' input type.
    """
    input_type = "date"


class BookingForm(forms.ModelForm):
    """
    A form for creating and updating Booking model instances.
    """
    class Meta:
        model = Booking
        fields = (
            'workshop', 'participants',
            'appointment_date', 'appointment_time'
        )
        widgets = {
            'appointment_date': DateInput()
        }
