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

    def test_workshop_detail_view(self):
        """Tests the rendering of a public workshop's detail page."""
        response = self.client.get(reverse('workshop_detail',
                                           args=[self.public_workshop.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Public Workshop", response.content)
        self.assertIn(b"Public workshop description", response.content)
        self.assertTemplateUsed(response, 'workshop/workshop_detail.html')
        self.assertTrue('workshop' in response.context)
        self.assertEqual(response.context['workshop'], self.public_workshop)

    def test_workshop_detail_view_private_workshop(self):
        """Tests that a private workshop detail returns a 404."""
        response = self.client.get(reverse('workshop_detail',
                                           args=[self.private_workshop.id]))
        self.assertEqual(response.status_code, 404)


class TestBookingViews(TestCase):

    def setUp(self):
        """Set up data for testing Booking views."""
        self.level = Level.objects.create(name='Beginner')
        self.workshop = Workshop.objects.create(
            level=self.level,
            name="Test Workshop",
            is_public=True,
            description="Test workshop description",
            excerpt="Test excerpt"
        )
        self.user = User.objects.create_user(
            username="testuser",
            password="password"
        )
        self.logged_in_client = self.client
        self.logged_in_client.login(username="testuser", password="password")
        self.booking = Booking.objects.create(
            workshop=self.workshop,
            booked_by=self.user,
            appointment_date=date.today() + timedelta(days=2),
            appointment_time='1pm-3pm',
            participants=2
        )

    def test_booking_display_authenticated(self):
        """Tests the booking display page for authenticated users."""
        response = self.logged_in_client.get(reverse('bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workshop/booking.html')
        self.assertIsInstance(response.context['booking_form'], BookingForm)
        self.assertTrue('bookings' in response.context)
        self.assertEqual(len(response.context['bookings']), 1)
        self.assertEqual(response.context['bookings'][0].booked_by, self.user)

    def test_booking_create_authenticated(self):
        """Tests the creation of a new booking via POST request."""
        booking_data = {
            'workshop': self.workshop.id,
            'participants': 3,
            'appointment_date': date.today() + timedelta(days=3),
            'appointment_time': '9am-11am'
        }
        response = self.logged_in_client.post(reverse('bookings'),
                                              booking_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.filter(booked_by=self.user).count(), 2)
        self.assertIn(b'Thank you for your booking!', response.content)
        self.assertTemplateUsed(response, 'workshop/booking.html')

    def test_booking_edit_authenticated_owner(self):
        """Tests editing a booking by its owner."""
        updated_date = date.today() + timedelta(days=5)
        booking_data = {
            'workshop': self.workshop.id,
            'participants': 1,
            'appointment_date': updated_date,
            'appointment_time': '7pm-9pm'
        }
        response = self.logged_in_client.post(
            reverse('update_booking', args=[self.booking.id]), 
            booking_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.appointment_date, updated_date)
        self.assertIn(b'booking Updated!', response.content)
        self.assertTemplateUsed(response, 'workshop/booking.html')

    def test_booking_delete_authenticated_owner(self):
        """Tests deleting a booking by its owner."""
        response = self.logged_in_client.post(
            reverse('delete_booking',
                    args=[self.booking.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 0)
        self.assertIn(b'Booking deleted!', response.content)
        self.assertTemplateUsed(response, 'workshop/booking.html')
