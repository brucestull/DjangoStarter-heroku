# Configuring Django Settings for Production

## Resources:
* https://thinkster.io/tutorials/configuring-django-settings-for-production

## Process:

1. Create directory `my_current_project/settings`:  
`mkdir my_current_project/settings`

1. Move and rename `my_current_project/settings.py` to `common.py`:  
`Move-Item -Path .\my_current_project\settings.py -Destination .\my_current_project\settings\common.py`

1. Remove `SECRET_KEY` line from `my_current_project/settings/common.py`.

1. Modify `BASE_DIR` in `my_current_project/settings/common.py` to define correct `BASE_DIR` since we nested `settings.py` one level down:  
`BASE_DIR = Path(__file__).resolve().parent.parent.parent`

1. Create `development.py` and `production.py` in `my_current_project/settings`:  
    * `settings/development.py`
        ```
        from my_current_project.settings.common import *

        DEBUG = True

        # Create your own `SECRET_KEY` here for use in Development. Create a different specific one for production only and use it in production only.
        SECRET_KEY = ""

        # To create a new `SECRET_KEY`:
        """
            python .\manage.py shell
            from django.core.management.utils import get_random_secret_key
            print(get_random_secret_key())
        """
        ```
    * `settings/production.py`
        ```
        from my_current_project.settings.common import *

        DEBUG = False

        # Create a specific `SECRET_KEY` for production and use it in production only.
        SECRET_KEY = os.environ.get('SECRET_KEY')

        # To create a new `SECRET_KEY`:
        """
            python .\manage.py shell
            from django.core.management.utils import get_random_secret_key
            print(get_random_secret_key())
        """
        ```

1. Change `os.environ.setdefault()` in `my_current_project/wsgi.py`:  
`os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_current_project.settings.development')`

1. Change `def main()` in `manage.py`:  
    ```
    def main():
        ...
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_current_project.settings.development')
        ...
    ```

1. Push changes to Heroku:  
`git push heroku main`

1. Set `DJANGO_SETTINGS_MODULE` to `'my_current_project.settings.production'` on production server. This will set up server to run the production settings since we will set a non-empty value for `DJANGO_SETTINGS_MODULE`:  
`heroku config:set DJANGO_SETTINGS_MODULE='my_current_project.settings.production'`

1. Test deployed application:  
    * https://django-custom-user-starter.herokuapp.com/

1. Verify `DEBUG` is `False`:  
    ```
    heroku login

    heroku run python manage.py shell

    from django.conf import settings as s

    print(s.DEBUG)
    ```

1. Verify the `SECRET_KEY` which Django is using is the value in Heroku Config Vars:  
    ```
    heroku login

    heroku run python manage.py shell

    from django.conf import settings as s

    print(s.SECRET_KEY)
    ```
