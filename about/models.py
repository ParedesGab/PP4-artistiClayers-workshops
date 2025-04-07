from django.db import models


# Create your models here.

# Create your models here.
class About(models.Model):
    """
    Stores a single about me entry.
    """
    title = models.CharField(max_length=200)
    # featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return f"{self.title} | Updated on {self.updated_on}"
