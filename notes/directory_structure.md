# Project Directory Structure

* `tree /f /a`:  
    ```
    PS C:\Users\Bruce\Programming\my-local-repository> tree /f /a
    ...
    C:.
    |   .gitignore
    |   LICENSE
    |   manage.py
    |   Pipfile
    |   Pipfile.lock
    |   Procfile
    |   README.md
    |
    +---my_current_project
    |   |   asgi.py
    |   |   urls.py
    |   |   wsgi.py
    |   |   __init__.py
    |   |
    |   \---settings
    |           common.py
    |           development.py
    |           production.py
    |
    +---notes
    |       add_database_settings_to_config_vars.md
    |       add_django_settings_module_to_config_vars.md
    |       add_secret_key_to_config_vars.md
    |       clone_django_custom_user_starter_repo.md
    |       create_empty_remote_repo_push_existing_application.md
    |       create_heroku_application_server_instance.md
    |       modify_allowed_hosts.md
    |       provision_database_server_instance.md
    |       push_to_heroku_and_createsuperuser.md
    |       run_application_locally.md
    |
    +---templates
    |   |   base.html
    |   |   home.html
    |   |
    |   \---registration
    |           login.html
    |           signup.html
    |
    \---users
        |   admin.py
        |   apps.py
        |   forms.py
        |   models.py
        |   tests.py
        |   urls.py
        |   views.py
        |   __init__.py
        |
        \---migrations
                0001_initial.py
                __init__.py
    ```


## Links:
[README.md](../README.md)