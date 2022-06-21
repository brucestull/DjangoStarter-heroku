# Create Heroku Application Server Instance

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


1. [Add Properties to Heroku Config Vars and Deploy Application](add_properties_to_heroku_config_vars.md)


## Links:
[README.md](../README.md)