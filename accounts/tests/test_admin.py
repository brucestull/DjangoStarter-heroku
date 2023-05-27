from django.test import TestCase

from accounts.models import CustomUser
from accounts.admin import CustomUserAdmin
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


TEST_USERNAME_ONE = 'OneUser'
TEST_PASSWORD_ONE = 'one_test_password'
TEST_FIRST_NAME_ONE = 'One'

TEST_USERNAME_TWO = 'TwoUser'
TEST_PASSWORD_TWO = 'two_test_password'
TEST_FIRST_NAME_TWO = 'Two'

class TestCustomUserAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        cls.user = CustomUser.objects.create(
            username=TEST_USERNAME_ONE,
            first_name=TEST_FIRST_NAME_ONE,
        )

    def test_uses_correct_model(self):
        """
        `CustomUserAdmin` `model` should be `CustomUser`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertEqual(custom_user_admin.model, CustomUser)

    def test_uses_correct_add_form(self):
        """
        `CustomUserAdmin` `add_form` should be `CustomUserCreationForm`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertEqual(custom_user_admin.add_form, CustomUserCreationForm)

    def test_uses_correct_change_form(self):
        """
        `CustomUserAdmin` `form` should be `CustomUserChangeForm`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertEqual(custom_user_admin.form, CustomUserChangeForm)

    def test_list_display_includes_username(self):
        """
        `CustomUserAdmin` `list_display` should include `username`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIn("username", custom_user_admin.list_display)

    def test_list_display_includes_is_staff(self):
        """
        `CustomUserAdmin` `list_display` should include `is_staff`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIn("is_staff", custom_user_admin.list_display)

