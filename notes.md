# Django Custom User Starter Notes

## NOTE:
* I've used '.' in place of '/' in some directory paths below. It's a style decision. Please use '/' or '\\' in place of '.' whenever needed in your filesystem interface.

## Set up Django:

1. Create pipenv and install Django and Docutils:
    `pipenv install django==3.2 docutils==0.18.1`

1. Note virtual environment location and starting command:
    * Virtual Environment activation:
        * Powershell: `C:\<path to virtual environment>\Scripts\activate.ps1`
        * BASH: `source C:/<path to virtual environment>/Scripts/activate`

1. Activate virtual environment:
    `C:\<path to virtual environment>\Scripts\activate.ps1`

1. Create project skeleton:
    `django-admin startproject my_current_project .`

1. Create `users` app:
    `python manage.py startapp users`

1. Test for green rocket:
    * Start server at some port (I have chosen optional non-default 8010):
    `python manage.py runserver 8010`
    * Verify green rocket:
    `http://localhost:8010/`

1. Stop the server:
    * Ctrl + c

1. Modify `my_current_project.settings.py`:
    ```
    INSTALLED_APPS = [
        ...
        'users.apps.UsersConfig', # Our addition from users.apps.UsersConfig
        ...
    ]

    AUTH_USER_MODEL = "users.CustomUser"    # Our addition
    ```

1. Modify `users.models.py`:
    * Our `CustomUser` which inherits `AbstractUser` has lots of functionality already built in. See some other documentation for info.
    ```
    from django.contrib.auth.models import AbstractUser

    class CustomUser(AbstractUser):
        pass
        # add additional fields in here

        def __str__(self):
            return self.username
    ```

1. Create `users.forms.py`:
    ```
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    from .models import CustomUser

    class CustomUserCreationForm(UserCreationForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email")

    class CustomUserChangeForm(UserChangeForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email")
    ```

1. Modify `users.admin.py`:
    ```
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin

    from .forms import CustomUserCreationForm, CustomUserChangeForm
    from .models import CustomUser

    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser
        list_display = ["email", "username",]

    admin.site.register(CustomUser, CustomUserAdmin)
    ```

1. Create migrations for `users` app:
    `python manage.py makemigrations users`

1. View the migrations which will be applied to `users` app:
    * Get current migration number from `users.migrations`.
    `python manage.py sqlmigrate users 0001`

1. Apply the migrations to `users` app:
    `python manage.py migrate`

1. Create `superuser`:
    `python manage.py createsuperuser`

1. Modify `my_current_project.settings.py`:
    * Direct Django templates engine to appropriate directory (in 'TEMPLATES' section).
        ```
        TEMPLATES = [
            {
                ...
                'DIRS': [BASE_DIR / "templates"],   # Our change
                ...
            },
        ]
        ```
    * Set login and logout redirects (at bottom of file):
        ```
        LOGIN_REDIRECT_URL = "home"     # Our addition
        LOGOUT_REDIRECT_URL = "home"    # Our addition
        ```

1. Create directories and files:
    * Directories:
        `my_current_project.templates`
        `my_current_project.templates.registration`
    * Files:
        `my_current_project.templates.base.html`
        `my_current_project.templates.home.html`
        `my_current_project.templates.registration.login.html`
        `my_current_project.templates.registration.signup.html`

1. Add contents to `my_current_project.templates.base.html`:
    ```
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>{% block title %}Django Auth Tutorial{% endblock %}</title>
        </head>
        <body>
            <main>
                {% block content %}
                {% endblock %}
            </main>
        </body>
    </html>
    ```

1. Add contents to `my_current_project.templates.home.html`:
    ```
    {% extends "base.html" %}

    {% block title %}Home{% endblock %}

    {% block content %}
        {% if user.is_authenticated %}
            Hi {{ user.username }}!
            <p><a href="{% url 'logout' %}">Log Out</a></p>
        {% else %}
            <p>You are not logged in</p>
            <a href="{% url 'login' %}">Log In</a> |
            <a href="{% url 'signup' %}">Sign Up</a>
        {% endif %}
    {% endblock %}
    ```

1. Add contents to `my_current_project.templates.registration.login.html`:
    ```
    {% extends "base.html" %}

    {% block title %}Log In{% endblock %}

    {% block content %}
        <h2>Log In</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Log In</button>
        </form>
    {% endblock %}
    ```

1. Add contents to `my_current_project.templates.registration.signup.html`:
    ```
    {% extends "base.html" %}

    {% block title %}Sign Up{% endblock %}

    {% block content %}
        <h2>Sign Up</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Sign Up</button>
        </form>
    {% endblock %}
    ```

1. Modify `my_current_project.urls.py` to match something similar:
    ```
    from django.contrib import admin
    from django.urls import path, include
    from django.views.generic.base import TemplateView

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('users/', include('users.urls')),
        path('users/', include('django.contrib.auth.urls')),
        path('', TemplateView.as_view(template_name='home.html'), name='home'),
    ]
    ```

1. Create `users.urls.py`:
    ```
    from django.urls import path

    from .views import SignUpView

    urlpatterns = [
        path("signup/", SignUpView.as_view(), name="signup"),
    ]
    ```

1. Modify `users.views.py`:
    ```
    from django.urls import reverse_lazy
    from django.views.generic.edit import CreateView

    from .forms import CustomUserCreationForm

    class SignUpView(CreateView):
        form_class = CustomUserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'registration/signup.html'
    ```

1. Test user login/logout/signup:
    `python manage.py runserver 8010`

1. Test admin interface:
    * `http://localhost:8010/admin/`

## Set up docutils:
1. Modify `my_current_project.settings.py`:
    ```
    INSTALLED_APPS = [
        ...
        'django.contrib.admindocs',
        ...
    ]
    ```

1. Modify `my_current_project.urls.py` (insert before 'admin/' entry):
    ```
    urlpatterns = [
        ...
        path('admin/doc/', include('django.contrib.admindocs.urls'))
        ...
    ]
    ```

