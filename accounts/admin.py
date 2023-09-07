from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "username",
        "email",
        "registration_accepted",
        "is_staff",
    )

    def get_fieldsets(self, request, obj=None):
        """
        Override `get_fieldsets()` to add `registration_accepted` to a
        `Moderator Permissions` section of `CustomUser` change view.
        """
        # Get the default `fieldsets` from the superclass
        # `django.contrib.auth.UserAdmin`:
        fieldsets = super().get_fieldsets(request, obj)
        # Convert fieldsets to list:
        fieldsets_as_list = list(fieldsets)
        # Create single tuple for `moderator_permissions`:
        moderator_permissions = (
            "Moderator Permissions",
            {"fields": ("registration_accepted",)},
        )
        # Insert `moderator_permissions` into `fieldsets_as_list` at index 2,
        # this will be after "Personal info" and before "Permissions":
        fieldsets_as_list.insert(2, moderator_permissions)
        return fieldsets_as_list
