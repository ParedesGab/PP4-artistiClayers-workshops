from django.test import TestCase
from datetime import date, timedelta
from .forms import BookingForm
from .models import Workshop, Level


class TestBookingForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.level = Level.objects.create(name='Beginner')
        cls.workshop = Workshop.objects.create(
            level=cls.level,
            name='Basics',
            description='Learn the basics of clay.',
            excerpt='A beginner-friendly workshop.',
            is_public=True
        )

    def test_form_is_valid(self):
        """ Test for all fields being valid """
        today = date.today()
        appointment_date = today + timedelta(days=1)
        form_data = {
            'workshop': self.workshop.id,
            'participants': 2,
            'appointment_date': appointment_date,
            'appointment_time': '9am-11am'
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid(),
                        msg="Form is not valid with valid data"
                        )

    def test_workshop_is_required(self):
        """
        Test that the 'workshop' field is required
        """
        today = date.today()
        form_data = {
            'workshop': '',
            'participants': 2,
            'appointment_date': today + timedelta(days=1),
            'appointment_time': '9am-11am'
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(),
                         msg="'workshop' was not provided, "
                         "but the form is valid"
                         )
        self.assertIn('workshop', form.errors)

    def test_participants_is_required(self):
        """
        Test that the 'participants' field is required
          """
        today = date.today()
        form_data = {
            'workshop': self.workshop.id,
            'participants': '',
            'appointment_date': today + timedelta(days=1),
            'appointment_time': '9am-11am'
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(),
                         msg="'participants' was not provided, "
                         "but the form is valid"
                         )
        self.assertIn('participants', form.errors)

    def test_appointment_date_is_required(self):
        """
        Test that the 'appointment_date' field is required
        """
        form_data = {
            'workshop': self.workshop.id,
            'participants': 2,
            'appointment_date': '',
            'appointment_time': '9am-11am'
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(),
                         msg="'appointment_date' was not provided, "
                         "but the form is valid")
        self.assertIn('appointment_date', form.errors)

    def test_appointment_time_is_required(self):
        """
        Test that the 'appointment_time' field is required
        """
        today = date.today()
        form_data = {
            'workshop': self.workshop.id,
            'participants': 2,
            'appointment_date': today + timedelta(days=1),
            'appointment_time': ''
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(),
                         msg="'appointment_time' was not provided, "
                         " but the form is valid"
                         )
        self.assertIn('appointment_time', form.errors)

    def test_participants_min_value(self):
        """
        Test for minimum value of 'participants'
        """
        today = date.today()
        form_data = {
            'workshop': self.workshop.id,
            'participants': 0,
            'appointment_date': today + timedelta(days=1),
            'appointment_time': '9am-11am'
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(),
                         msg="'participants' less than minimum, "
                         " but form is valid")
        self.assertIn('participants', form.errors)
        self.assertEqual(form.errors['participants'],
                         ['Ensure this value is greater than or equal to 1.']
                         )

    def test_participants_max_value(self):
        """
        Test for maximum value of 'participants'
        """
        today = date.today()
        form_data = {
            'workshop': self.workshop.id,
            'participants': 11,
            'appointment_date': today + timedelta(days=1),
            'appointment_time': '9am-11am'
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(),
                         msg="'participants' greater than maximum, "
                         "but form is valid"
                         )
        self.assertIn('participants', form.errors)
        self.assertEqual(form.errors['participants'],
                         ['Ensure this value is less than or equal to 10.']
                         )

    def test_appointment_date_not_in_past(self):
        """
        Test that 'appointment_date' cannot be in the past
        """
        yesterday = date.today() - timedelta(days=1)
        form_data = {
            'workshop': self.workshop.id,
            'participants': 2,
            'appointment_date': yesterday,
            'appointment_time': '9am-11am'
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(),
                         msg="'appointment_date' in the past, "
                         "but form is valid"
                         )
        self.assertIn('appointment_date', form.errors)
        self.assertEqual(form.errors['appointment_date'],
                         ['The date cannot be in the past']
                         )
