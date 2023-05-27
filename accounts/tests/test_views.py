from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

TEST_USERNAME_ONE = 'OneUser'
TEST_PASSWORD_ONE = 'one_test_password'
TEST_FIRST_NAME_ONE = 'One'

TEST_USERNAME_TWO = 'TwoUser'
TEST_PASSWORD_TWO = 'two_test_password'
TEST_FIRST_NAME_TWO = 'Two'

THE_SITE_NAME = "DjangoCustomUserStarter"

SIGN_UP_VIEW_URL = "/accounts/signup/"
SIGN_UP_VIEW_NAME = "signup"
SIGN_UP_VIEW_TEMPLATE = "registration/signup.html"

CUSTOM_LOGIN_VIEW_URL = "/accounts/login/"
CUSTOM_LOGIN_VIEW_NAME = "login"

USER_UPDATE_VIEW_URL = "/accounts/1/edit/"
USER_UPDATE_VIEW_NAME = "edit"
USER_UPDATE_VIEW_TEMPLATE = "registration/update.html"

USER_DETAIL_VIEW_URL = "/accounts/1/detail/"
USER_DETAIL_VIEW_NAME = "detail"
USER_DETAIL_VIEW_TEMPLATE = "accounts/customuser_detail.html"


class CustomUserSignUpViewTest(TestCase):
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
                "username": TEST_USERNAME_ONE,
                "password1": TEST_PASSWORD_ONE,
                "password2": TEST_PASSWORD_ONE,
                "first_name": TEST_FIRST_NAME_ONE,
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


class CustomUserLoginViewTest(TestCase):
    """
    Tests for `CustomUserLoginView`.
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


class CustomUserUpdateViewTest(TestCase):
    """
    Tests for `CustomUserUpdateView`.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create a test user and add it as an attribute of the `cls`.
        """
        cls.a_test_user = CustomUser.objects.create_user(
            username=TEST_USERNAME_ONE,
            password=TEST_PASSWORD_ONE,
        )

    def test_url_redirects_non_authenticated_user(self):
        """
        URL USER_UPDATE_VIEW_URL should redirect for non-authenticated user.
        """
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertRedirects(
            response,
            CUSTOM_LOGIN_VIEW_URL + "?next=" + USER_UPDATE_VIEW_URL,
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    # TODO: Test uses correct form.

    def test_view_uses_correct_template(self):
        """
        View should use USER_UPDATE_VIEW_TEMPLATE.
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, USER_UPDATE_VIEW_TEMPLATE)

    def test_user_is_self_object(self):
        """
        User should only be able to edit their own account.
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"], self.a_test_user)

    def test_view_returns_403_for_user_updating_another_user(self):
        """
        User should not be able to edit another user's account.
        """
        another_test_user = CustomUser.objects.create_user(
            username=TEST_USERNAME_TWO,
            password=TEST_PASSWORD_TWO,
        )
        self.client.force_login(another_test_user)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 403)        

    def test_the_site_name_in_context(self):
        """
        View `context` should have a value for THE_SITE_NAME.
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], THE_SITE_NAME)


class CustomUserDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Create a test user and add it as an attribute of the `cls`.
        """
        cls.a_test_user = CustomUser.objects.create_user(
            username=TEST_USERNAME_ONE,
            password=TEST_PASSWORD_ONE,
        )

    def test_url_redirects_non_authenticated_user(self):
        """
        URL USER_UPDATE_VIEW_URL should redirect for non-authenticated user.
        """
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertRedirects(
            response,
            CUSTOM_LOGIN_VIEW_URL + "?next=" + USER_DETAIL_VIEW_URL,
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_view_uses_correct_template(self):
        """
        View should use USER_DETAIL_VIEW_TEMPLATE.
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, USER_DETAIL_VIEW_TEMPLATE)

    def test_user_is_self_object(self):
        """
        User should only be able to view their own account.
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"], self.a_test_user)

    def test_view_returns_403_for_user_viewing_another_user(self):
        """
        User should not be able to view another user's account.
        """
        another_test_user = CustomUser.objects.create_user(
            username=TEST_USERNAME_TWO,
            password=TEST_PASSWORD_TWO,
        )
        self.client.force_login(another_test_user)
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 403)

