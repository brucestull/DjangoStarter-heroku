# Create Heroku Application Server Instance

## Resources:
* [Deploy a Django Project on Heroku - PDX Code Guild - Class Otter](https://github.com/PdxCodeGuild/class_otter/blob/main/5%20Capstone/Heroku%20Deployment.md)
* [Deploying with Git - devcenter.heroku.com](https://devcenter.heroku.com/articles/git)

## Process:

1. Open terminal in root of project:
    * Sample location:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming\my-new-app-repository
        ```

1. Verify current terminal session in root of repository, where `manage.py`, `Pipfile`, `Pipfile.lock`, and `Procfile` are located:  
    `Get-ChildItem`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> Get-ChildItem

            Directory: C:\Users\Bruce\Programming\my-new-app-repository

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d----          2022-06-20    21:14                my_current_project
        d----          2022-06-20    21:14                notes
        d----          2022-06-20    21:14                templates
        d----          2022-06-20    21:14                users
        -a---          2022-06-20    21:14           1470 .gitignore
        -a---          2022-06-20    21:51         131072 db.sqlite3
        -a---          2022-06-20    21:14          35823 LICENSE
        -a---          2022-06-20    21:14            708 manage.py
        -a---          2022-06-20    21:14            260 Pipfile
        -a---          2022-06-20    21:14           4299 Pipfile.lock
        -a---          2022-06-20    21:14            106 Procfile
        -a---          2022-06-20    21:14           2302 README.md
        ```

1. Log in to Heroku CLI if not already logged in (user may be redirected to browser for login credentials):  
    `heroku login`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> heroku login
        heroku: Press any key to open up the browser to login or q to exit:
        Opening browser to https://cli-auth.heroku.com/auth/cli/browser/3fb98706-0cce-4d22-9746-a34085061b51?requestor=SFMyNTY.g2gDbQAAAA03NS4xNzkuMTgwLjIwbgYAUEv5g4EBYgABUYA.CN-wrFbIUGrO54-dV0_Zblb94aNmCdfa14sxAXGuijE
        Logging in... done
        Logged in as user@email.app
        ```

1. Create Heroku app from local project repository:  
    `heroku create totally-new-heroku-app-name`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> heroku create totally-new-heroku-app-name
        Creating ⬢ totally-new-heroku-app-name... done
        https://totally-new-heroku-app-name.herokuapp.com/ | https://git.heroku.com/totally-new-heroku-app-name.git
        ```

1. Note Heroku application and Heroku git addresses:
    * Sample addresses:
        * Heroku application deployment address:
            * https://totally-new-heroku-app-name.herokuapp.com/
        * Heroku application git repository address:
            * https://git.heroku.com/totally-new-heroku-app-name.git

1. Verify Heroku git repository is set as a git remote in addition to the remote repository we created earlier:  
    `git remote -v`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> git remote -v
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (fetch)
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (push)
        origin  https://github.com/brucestull/new-remote-repository.git (fetch)
        origin  https://github.com/brucestull/new-remote-repository.git (push)
        ```

1. [Provision Database Server Instance](provision_database_server_instance.md)

## Links:
[README.md](../README.md)