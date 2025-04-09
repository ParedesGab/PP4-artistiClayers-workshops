from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    """
    Renders the About page
    """
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.title
