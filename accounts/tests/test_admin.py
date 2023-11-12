from django.test import TestCase

from accounts.models import CustomUser
from accounts.admin import CustomUserAdmin
from accounts.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)


TEST_USER_USERNAME = "TestUser"
TEST_USER_PASSWORD = "TestUserPassword"
TEST_USER_EMAIL = "TestUser@email.app"


class TestCustomUserAdmin(TestCase):
    """
    Inherit from `django.test.TestCase` to access `self.client` and
    `self.assert*` methods. `self` will be an instance of `django.test.TestCase`
    and `django.test.TestCase` inherits from `unittest.TestCase`.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        cls.user = CustomUser.objects.create_user(
            username=TEST_USER_USERNAME,
            password=TEST_USER_PASSWORD,
        )

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

    def test_uses_correct_model(self):
        """
        `CustomUserAdmin` `model` should be `CustomUser`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertEqual(custom_user_admin.model, CustomUser)

    def test_list_display_has_correct_fields_as_tuple(self):
        """
        `CustomUserAdmin` `list_display` should be a tuple.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIsInstance(custom_user_admin.list_display, tuple)
        expected_tuple = (
            "username",
            "email",
            "registration_accepted",
            "is_staff",
        )
        self.assertEqual(custom_user_admin.list_display, expected_tuple)

    # Here, we show another way to test the parts of `CustomUserAdmin.list_display`
    # below.
    def test_list_display_includes_username(self):
        """
        `CustomUserAdmin` `list_display` should include `username`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIn("username", custom_user_admin.list_display)

    def test_list_display_includes_email(self):
        """
        `CustomUserAdmin` `list_display` should include `email`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIn("email", custom_user_admin.list_display)

    def test_list_display_includes_registration_accepted(self):
        """
        `CustomUserAdmin` `list_display` should include `registration_accepted`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIn("registration_accepted", custom_user_admin.list_display)

    def test_list_display_includes_is_staff(self):
        """
        `CustomUserAdmin` `list_display` should include `is_staff`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIn("is_staff", custom_user_admin.list_display)

    def test_get_fieldsets_is_list_of_tuples(self):
        """
        `CustomUserAdmin` `get_fieldsets()` method should return a list of tuples.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        fieldsets = custom_user_admin.get_fieldsets(request=None, obj=None)
        self.assertIsInstance(fieldsets, list)
        self.assertIsInstance(fieldsets[0], tuple)

    def test_get_fieldsets_has_moderator_permissions_in_second_element(self):
        """
        `CustomUserAdmin` `get_fieldsets()` method should return a list of tuples that
        includes `Moderator Permissions`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        fieldsets = custom_user_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("Moderator Permissions", fieldsets_as_list[1])

    def test_get_fieldsets_moderator_permissions_tuple(self):
        """
        `CustomUserAdmin` `get_fieldsets()` method should return a list of tuples that
        includes `Moderator Permissions` as a tuple.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        expected_moderator_permissions_tuple = (
            "Moderator Permissions",
            {"fields": ("registration_accepted",)},
        )
        fieldsets = custom_user_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertEqual(
            fieldsets_as_list[1],
            expected_moderator_permissions_tuple,
        )
