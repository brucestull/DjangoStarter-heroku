# Add Properties to Heroku Config Vars

## Resources:
* [Heroku](https://www.heroku.com/)
* [Deploy a Django App to Heroku - Video - Pretty Printed](https://www.youtube.com/watch?v=GMbVzl_aLxM)

## Process:
1. Log in to Heroku and open the dashboard for the application:
    * My dashboard link:
        * https://dashboard.heroku.com/apps/totally-new-heroku-app-name
1. Open the "Settings" tab.
![01_heroku_application_dashboard_choose_settings](https://user-images.githubusercontent.com/47562501/174670415-0d1161b8-f961-4e51-9cb3-cc2378226e45.png)

1. Click "Reveal Config Vars". We will be adding two "Config Vars".
![02_heroku_settings_click_reveal_config_vars](https://user-images.githubusercontent.com/47562501/174670444-789944c3-a649-4940-84c0-56fcf3003885.png)

1. Note the database information already provided. We will use that later when we set up database settings in `production.py`.
![03_heroku_config_vars_database_url](https://user-images.githubusercontent.com/47562501/174670891-029b14cb-476e-4548-b03d-9639e96cce29.png)

1. Note the empty spaces where we will input the `KEY` and `VALUE` pairs for environment "Config Vars".
![04_heroku_config_vars_key_value_fields](https://user-images.githubusercontent.com/47562501/174670940-ffeaaff4-c703-44a7-91cc-fd9a610caff5.png)

1. First config var we will add is `DJANGO_SETTINGS_MODULE`. This is the dotted path from project root directory to project `production.py` file. But we will not include the `py` extension.
    * My example path:  
    `my_current_project.settings.production`
    * So, the `KEY` is:  
    `DJANGO_SETTINGS_MODULE`
    * And the `VALUE` is:  
    `my_current_project.settings.production`
![05_heroku_config_vars_add_django_settings_module_and_value](https://user-images.githubusercontent.com/47562501/174670971-b8096ff2-98d7-46a4-9158-bb022eb96083.png)

1. Click "Add" button.
![06_heroku_config_vars_click_add_button](https://user-images.githubusercontent.com/47562501/174671083-ca3a4e5e-5c66-4222-adb4-cf515416fe70.png)

1. Next config var is `SECRET_KEY`. We will generate this using Django shell.
    * In terminal session in root of repository, create a key and be prepared to copy it to Heroku application settings "Config Vars":
    1. Start Django shell:  
    `python manage.py shell`
    1. Import `get_random_secret_key`:  
    `from django.core.management.utils import get_random_secret_key`
    1. Use `get_random_secret_key` to get a new key:  
    `print(get_random_secret_key())`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> python manage.py shell
        Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>> from django.core.management.utils import get_random_secret_key
        >>> print(get_random_secret_key())
        o%tz4dbxm42$q=-_vj89l3@+)uw37a4b4!jurgw9&%+x9_f^o8
        ```

1. Add `SECRET_KEY` as the `KEY` and the output string in previous step as the `VALUE`.
![07_heroku_add_secret_key_and_value](https://user-images.githubusercontent.com/47562501/174671108-022c62ef-f224-4364-867f-244c46b47f41.png)

1. Click the "Add" button.
![08_heroku_config_vars_click_add_button](https://user-images.githubusercontent.com/47562501/174671124-f6fe9b3f-4199-42ab-9c82-66867498248f.png)

1. Dyno may restart itself during this process so there may be no need to restart it manually.
1. Add user's repository as remote:
    * LINK-FOR-INSTRUCTIONS-TO-PUSH-LOCAL-TO-USER-REMOTE-REPOSITORY


## Links:
[README.md](../README.md)
