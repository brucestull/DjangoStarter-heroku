# Add Properties to Heroku Config Vars and Deploy Application

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

1. Push application to Heroku server:  
`git push heroku main`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> git push heroku main
        Enumerating objects: 296, done.
        Counting objects: 100% (296/296), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (133/133), done.
        Writing objects: 100% (296/296), 106.83 KiB | 106.83 MiB/s, done.
        Total 296 (delta 165), reused 283 (delta 158), pack-reused 0
        remote: Compressing source files... done.
        remote: Building source:
        remote:
        remote: -----> Building on the Heroku-20 stack
        remote: -----> Determining which buildpack to use for this app
        remote: -----> Python app detected
        remote: -----> Using Python version specified in Pipfile.lock
        remote: cp: cannot stat '/tmp/build_dd30831d/requirements.txt': No such file or directory
        remote: -----> Installing python-3.10.5
        remote: -----> Installing pip 22.1.2, setuptools 60.10.0 and wheel 0.37.1
        remote: -----> Installing dependencies with Pipenv 2020.11.15
        remote:        Installing dependencies from Pipfile.lock (255abe)...
        remote:        Ignoring tzdata: markers 'sys_platform == "win32"' don't match your environment
        remote: -----> Installing SQLite3
        remote: -----> $ python manage.py collectstatic --noinput
        remote:        128 static files copied to '/tmp/build_dd30831d/staticfiles', 378 post-processed.
        remote:
        remote: -----> Discovering process types
        remote:        Procfile declares types -> release, web
        remote:
        remote: -----> Compressing...
        remote:        Done: 49.1M
        remote: -----> Launching...
        remote:  !     Release command declared: this new release will not be available until the command succeeds.
        remote:        Released v5
        remote:        https://totally-new-heroku-app-name.herokuapp.com/ deployed to Heroku
        remote:
        remote: Verifying deploy... done.
        remote: Running release command...
        remote:
        remote: Operations to perform:
        remote:   Apply all migrations: users
        remote: Running migrations:
        remote:   Applying contenttypes.0001_initial... OK
        remote:   Applying contenttypes.0002_remove_content_type_name... OK
        remote:   Applying auth.0001_initial... OK
        remote:   Applying auth.0002_alter_permission_name_max_length... OK
        remote:   Applying auth.0003_alter_user_email_max_length... OK
        remote:   Applying auth.0004_alter_user_username_opts... OK
        remote:   Applying auth.0005_alter_user_last_login_null... OK
        remote:   Applying auth.0006_require_contenttypes_0002... OK
        remote:   Applying auth.0007_alter_validators_add_error_messages... OK
        remote:   Applying auth.0008_alter_user_username_max_length... OK
        remote:   Applying auth.0009_alter_user_last_name_max_length... OK
        remote:   Applying auth.0010_alter_group_name_max_length... OK
        remote:   Applying auth.0011_update_proxy_permissions... OK
        remote:   Applying auth.0012_alter_user_first_name_max_length... OK
        remote:   Applying users.0001_initial... OK
        remote: Operations to perform:
        remote:   Apply all migrations: admin, auth, contenttypes, sessions, users
        remote: Running migrations:
        remote:   Applying admin.0001_initial... OK
        remote:   Applying admin.0002_logentry_remove_auto_add... OK
        remote:   Applying admin.0003_logentry_add_action_flag_choices... OK
        remote:   Applying sessions.0001_initial... OK
        remote: Waiting for release.... done.
        To https://git.heroku.com/totally-new-heroku-app-name.git
        * [new branch]      main -> main
        ```
1. Check application deployment on Heroku server:
    * Sample Heroku application deployment URL from above:
        * https://totally-new-heroku-app-name.herokuapp.com/
1. Application needs an admin account so create a superuser account using preferred username:  
`heroku run python manage.py createsuperuser`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> heroku run python manage.py createsuperuser
        Running python manage.py createsuperuser on ⬢ totally-new-heroku-app-name... up, run.4629 (Free)
        Username: MyTotallyUniqueAdminName
        Email address: MyTotallyUniqueAdminName@email.app
        Password:
        Password (again):
        Superuser created successfully.
        ```
1. Log in the Heroku-deployed application with user-created admin:
    * Sample Heroku application deployment URL from above:
        * https://totally-new-heroku-app-name.herokuapp.com/
1. Investigate Django Admin interface:
    * Sample URL:
        * https://totally-new-heroku-app-name.herokuapp.com/admin/
1. Investigate Django Admin Documentation (from [Django Admin Documentation Generator](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/)):
    * Sample URLs:
        * https://totally-new-heroku-app-name.herokuapp.com/admin/doc/
    * Default properties (which are inherited from User model in [django.contrib.auth](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/)) of the CustomUser:
        * https://totally-new-heroku-app-name.herokuapp.com/admin/doc/models/users.customuser/
1. Application is running in DEBUG mode in production. User needs to add some properties to Heroku `Config Vars` in Heroku application settings.


1. [Modify Some Final Production Settings](modify_some_final_production_settings.md)

## Links:
[README.md](../README.md)
