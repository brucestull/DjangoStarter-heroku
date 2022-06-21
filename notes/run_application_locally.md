# Run Application Locally

## Resources:


## Process:
1. Open terminal in project root:
    * Sample location:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive
        ```
1. Create `pipenv` virtual environment using provided `Pipfile` configuration:  
`pipenv install`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> pipenv install
        Creating a virtualenv for this project...
        Pipfile: C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive\Pipfile
        Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.4) to create virtualenv...
        [   =] Creating virtual environment...created virtual environment CPython3.10.4.final.0-64 in 420ms
        creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\DjangoCustomUserStarter-archive-KQz57jfW, clear=False, no_vcs_ignore=False, global=False)
        seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
            added seed packages: pip==22.1.2, setuptools==62.3.4, wheel==0.37.1
        activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

        Successfully created virtual environment!
        Virtualenv location: C:\Users\Bruce\.virtualenvs\DjangoCustomUserStarter-archive-KQz57jfW
        Installing dependencies from Pipfile.lock (255abe)...
        ================================ 11/11 - 00:00:10
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
        ```
1. Note line with `Virtualenv location:`. This line will have the virtual environment location. This information may be useful later.
    * Sample location:
        ```
        C:\Users\Bruce\.virtualenvs\DjangoCustomUserStarter-archive-KQz57jfW
        ```
1. Activate virtual environment:  
`pipenv shell`
    * Sample output:
        ```
            PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.4
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.
            ```
1. Perform `users` application migration:  
`python manage.py migrate users`
1. Perform project migration:  
`python manage.py migrate`
1. Create superuser:  
`python manage.py createsuperuser`
1. Follow `createsuperuser` dialogue.
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> python manage.py createsuperuser
        Username: admin
        Email address: admin@email.app
        Password:
        Password (again):
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.
        ```
1. Test application server:  
`python manage.py runserver`
1. Open browser to server url:
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