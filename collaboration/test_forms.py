from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields being valid """
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'message': 'Hello, I have a question.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid(),
                        msg="Form is not valid with valid data")

    def test_first_name_is_required(self):
        """ Test that the 'first_name' field is required """
        form_data = {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'message': 'Hello!'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg="'first_name' was not provided, but the form is valid"
        )
        self.assertIn('first_name', form.errors)
    
    def test_last_name_is_required(self):
        """ Test that the 'last_name' field is required """
        form_data = {
            'first_name': 'John',
            'last_name': '',
            'email': 'test@example.com',
            'message': 'Hello!'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg="'last_name' was not provided, but the form is valid"
        )
        self.assertIn('last_name', form.errors)

    def test_email_is_required(self):
        """ Test that the 'email' field is required """
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': '',
            'message': 'Hello!'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg="'email' was not provided, but the form is valid"
        )
        self.assertIn('email', form.errors)

    def test_message_is_required(self):
        """ Test that the 'message' field is required """
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg="'message' was not provided, but the form is valid"
        )
        self.assertIn('message', form.errors)

    def test_invalid_email_format(self):
        """ Test that the form is invalid for incorrect email format """
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalid-email',
            'message': 'Hello!'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="Form is valid with an invalid email")
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
