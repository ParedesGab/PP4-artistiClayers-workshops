from django.db import models
from cloudinary.models import CloudinaryField


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
        Level, on_delete=models.CASCADE, related_name="workshop_levels"
    )
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.level_id
