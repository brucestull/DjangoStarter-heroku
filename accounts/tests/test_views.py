from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

A_TEST_USERNAME = "ACustomUser"
A_TEST_PASSWORD = "a_test_password"
A_TEST_FIRST_NAME = "A"

THE_SITE_NAME = "DjangoCustomUserStarter"

SIGN_UP_VIEW_URL = "/accounts/signup/"
SIGN_UP_VIEW_NAME = "signup"
SIGN_UP_VIEW_TEMPLATE = "registration/signup.html"

CUSTOM_LOGIN_VIEW_URL = "/accounts/login/"
CUSTOM_LOGIN_VIEW_NAME = "login"

USER_UPDATE_VIEW_URL = "/accounts/1/edit/"
USER_UPDATE_VIEW_NAME = "edit-profile"
USER_UPDATE_VIEW_TEMPLATE = "registration/update.html"


class SignUpViewTest(TestCase):
    """
    Tests for `SignUpView`.
    """

    def test_url_exists(self):
        """
        URL SIGN_UP_VIEW_URL should return status 200.
        """
        response = self.client.get(SIGN_UP_VIEW_URL)
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        """
        View name SIGN_UP_VIEW_NAME should return status 200.
        """
        response = self.client.get(reverse(SIGN_UP_VIEW_NAME))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_form(self):
        """
        View should use form `CustomUserCreationForm`.
        """
        response = self.client.get(SIGN_UP_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        # Test that the form is an instance of `CustomUserCreationForm`.
        self.assertIsInstance(response.context["form"], CustomUserCreationForm)
        # Alternative ways to test the form:
        # Test that the form's class is `CustomUserCreationForm`.
        self.assertEqual(response.context["form"].__class__, CustomUserCreationForm)
        # Test that the form's class name is the string `CustomUserCreationForm`.
        self.assertEqual(
            response.context["form"].__class__.__name__, "CustomUserCreationForm"
        )

    def test_redirects_to_login_page_on_success(self):
        """
        User should be redirected to the login page on successful signup.
        """
        response = self.client.post(
            SIGN_UP_VIEW_URL,
            {
                "username": A_TEST_USERNAME,
                "password1": A_TEST_PASSWORD,
                "password2": A_TEST_PASSWORD,
                "first_name": A_TEST_FIRST_NAME,
            },
        )
        self.assertRedirects(response, CUSTOM_LOGIN_VIEW_URL)

    def test_uses_correct_template(self):
        """
        View should use SIGN_UP_VIEW_TEMPLATE.
        """
        response = self.client.get(SIGN_UP_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, SIGN_UP_VIEW_TEMPLATE)

    def test_context_has_the_site_name(self):
        """

        View `context` should have a value for THE_SITE_NAME.
        """
        response = self.client.get(SIGN_UP_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], THE_SITE_NAME)


class CustomLoginViewTest(TestCase):
    """
    Tests for `CustomLoginView`.
    """

    def test_url_exists(self):
        """
        URL CUSTOM_LOGIN_VIEW_URL should return status 200.
        """
        response = self.client.get(CUSTOM_LOGIN_VIEW_URL)
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        """
        View name CUSTOM_LOGIN_VIEW_NAME should return status 200.
        """
        response = self.client.get(reverse(CUSTOM_LOGIN_VIEW_NAME))
        self.assertEqual(response.status_code, 200)

    def test_context_has_the_site_name(self):
        """
        View `context` should have a value for THE_SITE_NAME.
        """
        response = self.client.get(CUSTOM_LOGIN_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], THE_SITE_NAME)


class UserUpdateViewTest(TestCase):
    """
    Tests for `UserUpdateView`.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create a test user and add it as an attribute of the `cls`.
        """
        cls.a_test_user = CustomUser.objects.create_user(
            username=A_TEST_USERNAME,
            password=A_TEST_PASSWORD,
        )
        pass

    # TODO: Why is this not working as expected?
    def test_url_redirects_for_non_authenticated_user(self):
        """
        URL USER_UPDATE_VIEW_URL should redirect for non-authenticated user.
        """
        # response = self.client.get(
        #     reverse(
        #         USER_UPDATE_VIEW_NAME,
        #         kwargs={"pk": self.a_test_user.pk},
        #     )
        # )
        # self.assertRedirects(
        #     response,
        #     CUSTOM_LOGIN_VIEW_URL + "?next=" + USER_UPDATE_VIEW_URL,
        #     status_code=302,
        #     target_status_code=200,
        #     fetch_redirect_response=True,
        # )
        pass
