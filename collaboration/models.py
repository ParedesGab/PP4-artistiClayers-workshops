from django.db import models


class ContactRequest(models.Model):
    """
    Represents a contact request
    submitted by a user through the website.
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request from {self.first_name} {self.last_name}"
