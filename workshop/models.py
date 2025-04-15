from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


def validate_date_not_in_past(value):
    today = date.today()
    if value < today:
        raise ValidationError("The date cannot be in the past")


class Level(models.Model):
    """
    Stores a single workshop difficulty level.
    """
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name


class Workshop(models.Model):
    """
    Stores a single workshop entry.
    """
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, related_name="workshops"
    )
    name = models.CharField(max_length=50, blank=False, null=False,
                            default="New Workshop")
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Stores a single Booking entry.
    """
    APPOINTMENT_TIMES = [
        ("9am-11am", "9am - 11am"),
        ("1pm-3pm", "1pm - 3pm"),
        ("7pm-9pm", "7pm - 9pm")
    ]
    booked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    workshop = models.ForeignKey(
        Workshop, on_delete=models.CASCADE, related_name="workshop_bookings"
    )
    date_booked = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateField(validators=[validate_date_not_in_past])
    appointment_time = models.CharField(
        max_length=10,
        choices=APPOINTMENT_TIMES,
        default="9am-11am"
    )
    participants = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Please indicate number of participants up to 10",
    )
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["-appointment_date"]

    def __str__(self):
        return f"""
                {self.booked_by.username} booked '{self.workshop.name}'
                for {self.participants} participant(s)
                on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}
        """
