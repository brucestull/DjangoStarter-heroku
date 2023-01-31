# Override Admin Templates

* This example is for the `password_change_form.html` template, but the same process applies to all admin templates, where we are overriding them by using the same template name in our `accounts` app.

## Use default admin templates

* [`config/settings/common.py`](../config/settings/common.py):
  * List `django.contrib.admin` before `accounts.apps.AccountsConfig` in `INSTALLED_APPS`:

        ```python
        INSTALLED_APPS = [
            #...
            'django.contrib.admin',
            'accounts.apps.AccountsConfig',
            #...
        ]
        ```

* Uses default template [
    `django/contrib/admin/templates/registration/password_change_form.html`
    ](
      <https://github.com/django/django/blob/main/django/contrib/admin/templates/registration/password_change_form.html>
    )

* Browser Image:

## Override admin templates

* [`config/settings/common.py`](../config/settings/common.py):
  * List `accounts.apps.AccountsConfig` before `django.contrib.admin` in `INSTALLED_APPS`:

        ```python
        INSTALLED_APPS = [
            #...
            'accounts.apps.AccountsConfig',
            'django.contrib.admin',
            #...
        ]
        ```

* Uses our template [
      `accounts/templates/registration/password_change_form.html`
    ](
      ../accounts/templates/registration/password_change_form.html
    )

* Browser Image:
