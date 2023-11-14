from django.test import TestCase
from django.urls import reverse

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


class CustomUserSignUpViewTest(TestCase):
    """
    Tests for `SignUpView`.
    """

    def test_url_exists(self):
        """
        URL "/accounts/signup/" should return status 200.
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        """
        View name "signup" should return status 200.
        """
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_form(self):
        """
        View should use form `CustomUserCreationForm`.
        """
        response = self.client.get("/accounts/signup/")
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
            "/accounts/signup/",
            {
                "username": "DezziKitten",
                "password1": "MeowMeow42",
                "password2": "MeowMeow42",
                "email": "DezziKitten@purr.scratch",
            },
        )
        self.assertRedirects(response, "/accounts/login/")

    def test_uses_correct_template(self):
        """
        View should use "registration/signup.html".
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_context_has_the_site_name(self):
        """
        View `context` should have a value of "DjangoCustomUserStarter" for
        "the_site_name".
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], "DjangoCustomUserStarter")


class CustomUserLoginViewTest(TestCase):
    """
    Tests for `CustomUserLoginView`.
    """

    def test_url_exists(self):
        """
        URL "/accounts/login/" should return status 200.
        """
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        """
        View name "login" should return status 200.
        """
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_context_has_the_site_name(self):
        """
        View `context` should have a value "DjangoCustomUserStarter" for
        "the_site_name".
        """
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], "DjangoCustomUserStarter")


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
            username="DezziKitten",
            password="MeowMeow42",
            email="DezziKitten@purr.scratch",
        )

    def test_url_redirects_non_authenticated_user(self):
        """
        URL "/accounts/1/edit/" should redirect for non-authenticated user.
        """
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertRedirects(
            response,
            "/accounts/login/" + "?next=" + "/accounts/1/edit/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    # TODO: Test uses correct form.

    def test_view_uses_correct_template(self):
        """
        View should use "registration/update.html".
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/update.html")

    def test_user_is_self_object(self):
        """
        User should only be able to edit their own account.
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                "edit",
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
            username="BunbunKitten",
            password="MeowMeow42",
            email="BunbunKitten@purr.scratch",
        )
        self.client.force_login(another_test_user)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 403)

    def test_the_site_name_in_context(self):
        """
        View `context` should have a value of "DjangoCustomUserStarter" for
        "the_site_name".
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], "DjangoCustomUserStarter")


class CustomUserDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Create a test user and add it as an attribute of the `cls`.
        """
        cls.a_test_user = CustomUser.objects.create_user(
            username="DezziKitten",
            password="MeowMeow42",
            email="DezziKitten@purr.scratch",
        )

    def test_url_redirects_non_authenticated_user(self):
        """
        URL "/accounts/1/edit/" should redirect for non-authenticated user.
        """
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertRedirects(
            response,
            "/accounts/login/" + "?next=" + "/accounts/1/detail/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_view_uses_correct_template(self):
        """
        View should use "accounts/customuser_detail.html".
        """
        self.client.force_login(self.a_test_user)
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/customuser_detail.html")

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
            username="BunbunKitten",
            password="MeowMeow42",
            email="BunbunKitten@purr.scratch",
        )
        self.client.force_login(another_test_user)
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 403)
