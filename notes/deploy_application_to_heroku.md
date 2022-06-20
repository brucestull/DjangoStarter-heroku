# Deploy Application to Heroku

## Resources:
* [Deploy a Django Project on Heroku - PDX Code Guild - Class Otter](https://github.com/PdxCodeGuild/class_otter/blob/main/5%20Capstone/Heroku%20Deployment.md)
* [Deploying with Git - devcenter.heroku.com](https://devcenter.heroku.com/articles/git)

## Process:
1. Open terminal in root of project:
    * Sample location:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive
        ```
1. Verify current terminal session in root of repository, where `manage.py`, `Pipfile`, `Pipfile.lock`, and `Procfile` are located:
`Get-ChildItem`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> Get-ChildItem

            Directory: C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d----          2022-06-20    09:04                my_current_project
        d----          2022-06-20    09:13                notes
        d----          2022-06-20    09:28                staticfiles
        d----          2022-06-20    09:12                templates
        d----          2022-06-20    09:04                users
        -a---          2022-06-20    09:04           1470 .gitignore
        -a---          2022-06-20    09:37         131072 db.sqlite3
        -a---          2022-06-20    09:04          35823 LICENSE
        -a---          2022-06-20    09:04            708 manage.py
        -a---          2022-06-20    09:12            244 Pipfile
        -a---          2022-06-20    09:12           9119 Pipfile.lock
        -a---          2022-06-20    09:04            106 Procfile
        -a---          2022-06-20    09:13           1338 README.md
        ```
1. Log in to Heroku CLI (user may be redirected to browser for login credentials):
`heroku login`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> heroku login
        heroku: Press any key to open up the browser to login or q to exit:
        Opening browser to https://cli-auth.heroku.com/auth/cli/browser/ea1c92f9-369f-4354-af64-27c2f7e9fa89?requestor=SFMyNTY.g2gDbQAAAA03NS4xNzkuMTgwLjIwbgYAAB5vgYEBYgABUYA._GfT_caXNyoD0NTMnhA_tDb9mi1DjKoOQqR9lkQ7vPI
        Logging in... done
        Logged in as user@email.app
        ```
1. Create Heroku app from project repository:
`heroku create totally-new-heroku-app-name`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> heroku create totally-new-heroku-app-name
        Creating ⬢ totally-new-heroku-app-name... done
        https://totally-new-heroku-app-name.herokuapp.com/ | https://git.heroku.com/totally-new-heroku-app-name.git
        ```
1. Note Heroku application and heroku git URLs:
    * Sample URLs:
        * Heroku application deployment URL:
            * https://totally-new-heroku-app-name.herokuapp.com/
        * Heroku application git repository URL:
            * https://git.heroku.com/totally-new-heroku-app-name.git

1. Verify Heroku git repository is set as a git remote:
`git remote -v`
    * Sample output:
        ```
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (fetch)
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (push)
        origin  https://github.com/brucestull/DjangoCustomUserStarter-archive (fetch)
        origin  https://github.com/brucestull/DjangoCustomUserStarter-archive (push)
        ```
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

1. [Add Properties to Heroku Config Vars](add_properties_to_heroku_config_vars.md)


## Links:
[README.md](..\README.md)