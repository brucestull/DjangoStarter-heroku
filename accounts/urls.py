from django.urls import path

from accounts.views import SignUpView, UserUpdateView, CustomLoginView

urlpatterns = [
    # Try to override 'login' view.
    path("login/", CustomLoginView.as_view(), name="login"),

    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/edit/", UserUpdateView.as_view(), name="edit_profile"),
]