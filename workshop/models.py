from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


# Create your models here.

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
    booked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    workshop = models.ForeignKey(
        Workshop, on_delete=models.CASCADE, related_name="workshop_bookings"
    )
    date_booked = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateTimeField(default=timezone.now)
    participants = models.PositiveBigIntegerField(
        default=1,
        help_text="Please indicate number of participants",
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
