# Run Application Locally

## Resources:

## Process:

1. Open terminal in project root:
    * Sample location:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming\my-local-repository
        ```

1. Create `pipenv` virtual environment using provided `Pipfile` configuration:  
    `pipenv install`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> pipenv install
        Creating a virtualenv for this project...
        Pipfile: C:\Users\Bruce\Programming\my-local-repository\Pipfile
        Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.4) to create virtualenv...
        [==  ] Creating virtual environment...created virtual environment CPython3.10.4.final.0-64 in 2858ms
        creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\my-local-repository-G4xugRBF, clear=False, no_vcs_ignore=False, global=False)
        seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
            added seed packages: pip==22.1.2, setuptools==62.3.4, wheel==0.37.1
        activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

        Successfully created virtual environment!
        Virtualenv location: C:\Users\Bruce\.virtualenvs\my-local-repository-G4xugRBF
        Installing dependencies from Pipfile.lock (16fbc4)...
        ================================ 9/9 - 00:00:09
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
        ```

1. Note line with `Virtualenv location:`. This line will have the virtual environment location. This information may be useful later.
    * Sample location:
        ```
        C:\Users\Bruce\.virtualenvs\my-local-repository-G4xugRBF
        ```

1. Activate virtual environment:  
    `pipenv shell`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> pipenv shell
        Launching subshell in virtual environment...
        PowerShell 7.2.4
        Copyright (c) Microsoft Corporation.

        https://aka.ms/powershell
        Type 'help' to get help.
        ```

1. Perform `users` application migration:  
    `python manage.py migrate users`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> python manage.py migrate users
        Operations to perform:
        Apply all migrations: users
        Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0001_initial... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying auth.0012_alter_user_first_name_max_length... OK
        Applying users.0001_initial... OK
        ```

1. Perform project migration:  
    `python manage.py migrate`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> python manage.py migrate
        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions, users
        Running migrations:
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying sessions.0001_initial... OK
        ```

1. Create superuser:  
    `python manage.py createsuperuser`
    * Follow `createsuperuser` dialog.
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\my-local-repository> python manage.py createsuperuser
            Username: admin
            Email address: admin@email.app
            Password:
            Password (again):
            This password is too common.
            Bypass password validation and create user anyway? [y/N]: y
            Superuser created successfully.
            ```

1. Test application on local server:  
    `python manage.py runserver`

1. Open browser to server address:
    * http://localhost:8000/

1. Login using admin credentials created above.

1. Investigate Django Admin interface:
    * http://localhost:8000/admin/

1. Investigate the Django Admin Documentation features:
    * http://localhost:8000/admin/doc/
    * http://localhost:8000/admin/doc/models/users.customuser/

1. [Create Heroku Application Server Instance](create_heroku_application_server_instance.md)


## Links:
[README.md](../README.md)