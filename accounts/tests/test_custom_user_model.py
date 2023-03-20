from django.test import TestCase
from django.db import models

from accounts.models import CustomUser

A_TEST_USERNAME = 'ACustomUser'

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
        user = CustomUser.objects.create(
            username=A_TEST_USERNAME,
        )

    def test_dunder_string_method(self):
        """
        `CustomUser` model `__str__` method should return `username`.
        """
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.__str__(), user.username)
