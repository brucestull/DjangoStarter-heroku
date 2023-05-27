from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser
from config.settings.common import THE_SITE_NAME


class CustomUserSignUpView(CreateView):
    """
    View for user to create a new account.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add `the_site_name` to the it.
        """
        context = super().get_context_data(**kwargs)
        context['the_site_name'] = THE_SITE_NAME
        return context


class CustomUserLoginView(LoginView):
    """
    Override the default login view. This will allow us to add the site name to the context and then display it on the page.
    """

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add `the_site_name` to the it.
        """
        context = super().get_context_data(**kwargs)
        context['the_site_name'] = THE_SITE_NAME
        return context


class CustomUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for user to update an existing account.
    """

    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("login")
    template_name = "registration/update.html"

    def test_func(self):
        """
        Only allow the user to edit their own account.
        """
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add `the_site_name` to the it.
        """
        context = super().get_context_data(**kwargs)
        context['the_site_name'] = THE_SITE_NAME
        return context


class CustomUserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    View for user to view their account details.

    We are only specifying the `model` here because we are using the default template name that is created by Django.
    """
    model = CustomUser

    def test_func(self):
        """
        Only allow the user to view their own account details.
        """
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add `the_site_name` and/or `page_title` to the it.
        """
        context = super().get_context_data(**kwargs)
        # context['the_site_name'] = THE_SITE_NAME
        context['page_title'] = f"{self.object.username}'s User Information"
        return context
