# Create Heroku Application Server Instance

## Resources:
* [Deploy a Django Project on Heroku - PDX Code Guild - Class Otter](https://github.com/PdxCodeGuild/class_otter/blob/main/5%20Capstone/Heroku%20Deployment.md)
* [Deploying with Git - devcenter.heroku.com](https://devcenter.heroku.com/articles/git)

## Process:

1. Open terminal in root of project:
    * Sample location:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming\my-local-repository
        ```

1. Verify current terminal session in root of repository, where `manage.py`, `Pipfile`, `Pipfile.lock`, and `Procfile` are located:  
    `Get-ChildItem`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> Get-ChildItem

            Directory: C:\Users\Bruce\Programming\my-local-repository

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d----          2022-06-21    09:27                my_current_project
        d----          2022-06-21    09:27                notes
        d----          2022-06-21    09:27                templates
        d----          2022-06-21    09:27                users
        -a---          2022-06-21    09:27           1470 .gitignore
        -a---          2022-06-21    09:55         131072 db.sqlite3
        -a---          2022-06-21    09:27          35823 LICENSE
        -a---          2022-06-21    09:27            708 manage.py
        -a---          2022-06-21    09:27            260 Pipfile
        -a---          2022-06-21    09:27           4299 Pipfile.lock
        -a---          2022-06-21    09:27            106 Procfile
        -a---          2022-06-21    09:27           2405 README.md
        ```

1. Log in to Heroku CLI if not already logged in (user may be redirected to browser for login credentials):  
    `heroku login`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> heroku login
        heroku: Press any key to open up the browser to login or q to exit:
        ...
        Logging in... done
        Logged in as user@email.app
        ```

1. Create Heroku app from local project repository:  
    `heroku create totally-new-heroku-app-name`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> heroku create totally-new-heroku-app-name
        Creating ⬢ totally-new-heroku-app-name... done
        https://totally-new-heroku-app-name.herokuapp.com/ | https://git.heroku.com/totally-new-heroku-app-name.git
        ```

1. Note Heroku application and Heroku git addresses:
    * Sample addresses:
        * Heroku application deployment address:
            * https://totally-new-heroku-app-name.herokuapp.com/
        * Heroku application git repository address:
            * https://git.heroku.com/totally-new-heroku-app-name.git

1. Verify there are now two git remotes: `heroku` and `origin` (which we created earlier):  
    `git remote -v`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> git remote -v
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (fetch)
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (push)
        origin  https://github.com/brucestull/new-remote-repository.git (fetch)
        origin  https://github.com/brucestull/new-remote-repository.git (push)
        ```

    * NOTE: We currently will be pushing changes to the two separate remotes using different commands. There are ways to change workflow but that is beyond scope of this exercise.
        * `git push` (for `origin`)
        * `git push heroku main` (for `heroku`)

1. [Provision Database Server Instance](provision_database_server_instance.md)

## Links:
[README.md](../README.md)