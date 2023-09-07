from django.test import TestCase
from django.contrib.auth.models import AbstractUser

from accounts.models import CustomUser

TEST_USER_USERNAME = "CustomUser"
TEST_USER_EMAIL = "CustomUser@email.app"
TEST_USER_PASSWORD = "CustomUserPassword"

class CustomUserModelTest(TestCase):
    """
    Tests for `CustomUser` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        cls.user = CustomUser.objects.create(
            username=TEST_USER_USERNAME,
            email=TEST_USER_EMAIL,
            password=TEST_USER_PASSWORD,
        )

    def test_model_inherits_from_abstract_user(self):
        """
        `CustomUser` model should inherit from `AbstractUser`.
        """
        self.assertTrue(issubclass(CustomUser, AbstractUser))

    def test_registration_accepted_verbose_name(self):
        """
        `CustomUser.registration_accepted.verbose_name` should be
        "Registration Accepted".
        """
        expected_verbose_name = "Registration Accepted"
        self.assertEqual(
            CustomUser._meta.get_field("registration_accepted").verbose_name,
            expected_verbose_name,
        )

    def test_registration_accepted_help_text(self):
        """
        `CustomUser.registration_accepted.help_text` should be
        "Designates whether this user's site registration has been accepted.".
        """
        expected_help_text = "Designates whether this user's site registration has been accepted."
        self.assertEqual(
            CustomUser._meta.get_field("registration_accepted").help_text,
            expected_help_text,
        )

    def test_registration_accepted_default_false(self):
        """
        `CustomUser.registration_accepted.default` should be `False`.
        """
        expected_default = False
        self.assertEqual(
            CustomUser._meta.get_field("registration_accepted").default,
            expected_default,
        )

    def test_dunder_string_method(self):
        """
        `CustomUser` model `__str__` method should return `CustomUser.username`.
        """
        expected_dunder_string = TEST_USER_USERNAME
        self.assertEqual(
            str(self.user),
            expected_dunder_string,
        )
