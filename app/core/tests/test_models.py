from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    def test_create_user_with_email_success(self):
        """ Test creating a new user with an email is successful. """
        email = "oguzhancelikarslan@gmail.com"
        password = "deneme//*asd"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_new_user_with_normalized_email(self):
        email = "oguzhancelikarslan@GMAIL.com"
        password = "deneme//*asd"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_creating_super_user(self):
        email = "oguzhancelikarslan@GMAIL.com"
        password = "deneme//*asd"

        user = get_user_model().objects.create_super_user(
            email=email,
            password=password
        )

        self.assertTrue(user.is_active)
        self.assertTrue(user.is_stuff)

    def test_new_user_invalid_address(self):
        with self.assertRaises(ValueError):
            # this test pass if this piece raise an ValueError in case of passing invalid value to create_user function
            get_user_model().objects.create_user(email=None, password="asdasd")
