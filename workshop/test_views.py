from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Workshop, Booking, Level
from .forms import BookingForm
from datetime import date, timedelta


class TestWorkshopViews(TestCase):

    def setUp(self):
        """Set up data for testing Workshop views."""
        self.level = Level.objects.create(name='Beginner')
        self.public_workshop = Workshop.objects.create(
            level=self.level,
            name="Public Workshop",
            is_public=True,
            description="Public workshop description",
            excerpt="Public excerpt"
        )
        self.private_workshop = Workshop.objects.create(
            level=self.level,
            name="Private Workshop",
            is_public=False,
            description="Private workshop description",
            excerpt="Private excerpt"
        )
        self.user = User.objects.create_user(
            username="testuser",
            password="password"
        )
        self.logged_in_client = self.client
        self.logged_in_client.login(username="testuser", password="password")

    def test_workshop_list_view(self):
        """Tests the rendering of the public workshop list."""
        response = self.client.get(reverse('workshops'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Public Workshop", response.content)
        self.assertNotIn(b"Private Workshop", response.content)
        self.assertTemplateUsed(response, 'workshop/workshop_list.html')
        self.assertTrue('workshop_list' in response.context)
        self.assertEqual(len(response.context['workshop_list']), 1)
        self.assertIsInstance(response.context['workshop_list'][0], Workshop)
