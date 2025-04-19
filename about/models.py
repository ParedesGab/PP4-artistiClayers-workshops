from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Represents information for the About page,
    including a title, profile image, and description.
    """
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.title
