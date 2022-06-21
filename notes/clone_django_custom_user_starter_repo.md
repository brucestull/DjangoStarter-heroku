# Clone DjangoCustomUserStarter Repository

## Resources:

## Process:

1. Get remote repository URL:
    * https://github.com/brucestull/DjangoCustomUserStarter.git

1. Open terminal in parent directory where repository will be located:  
    * Sample location:
        ```
        PS C:\Users\Bruce\Programming> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming
        ```

1. Clone remote repository as a new directory into currrent directory:  
`git clone https://github.com/brucestull/DjangoCustomUserStarter.git my-new-app-repository`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming> git clone https://github.com/brucestull/DjangoCustomUserStarter.git my-new-app-repository
        Cloning into 'my-new-app-repository'...
        remote: Enumerating objects: 461, done.
        remote: Counting objects: 100% (80/80), done.
        remote: Compressing objects: 100% (39/39), done.
        remote: Total 461 (delta 50), reused 50 (delta 41), pack-reused 381
        Receiving objects: 100% (461/461), 143.98 KiB | 2.12 MiB/s, done.
        Resolving deltas: 100% (271/271), done.
        ```

1. Change directory into local repository directory:  
    ```
    PS C:\Users\Bruce\Programming> Set-Location .\my-new-app-repository\
    ```

1. Verify directory contents:  
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
        -a---          2022-06-20    21:14          35823 LICENSE
        -a---          2022-06-20    21:14            708 manage.py
        -a---          2022-06-20    21:14            260 Pipfile
        -a---          2022-06-20    21:14           4299 Pipfile.lock
        -a---          2022-06-20    21:14            106 Procfile
        -a---          2022-06-20    21:14           2302 README.md
        ```

1. Verify current remote repository:  
`git remote -v`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> git remote -v
        origin  https://github.com/brucestull/DjangoCustomUserStarter.git (fetch)
        origin  https://github.com/brucestull/DjangoCustomUserStarter.git (push)
        ```

1. Remove git remote repository links for `origin` repository so user can push code to their own repository:  
`git remote remove origin`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> git remote remove origin
        ```

1. Verify current remote repository:  
`git remote -v`
    * Sample output:
    ```
    PS C:\Users\Bruce\Programming\my-new-app-repository> git remote -v
    ```

1. [Create Empty Remote GitHub Repository and Push Existing Application](create_empty_remote_repo_push_existing_application.md)


## Links:
[README.md](../README.md)