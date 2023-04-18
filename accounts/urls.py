from django.urls import path

from accounts.views import CustomUserSignUpView, CustomLoginView
from accounts.views import CustomUserUpdateView, CustomUserDetailView

urlpatterns = [
    # Try to override 'login' view.
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path("<int:pk>/edit/", CustomUserUpdateView.as_view(), name="edit"),
    path("<int:pk>/detail/", CustomUserDetailView.as_view(), name="detail"),
]