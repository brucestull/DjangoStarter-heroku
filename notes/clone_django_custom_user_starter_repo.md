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
    `git clone https://github.com/brucestull/DjangoCustomUserStarter.git my-local-repository`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming> git clone https://github.com/brucestull/DjangoCustomUserStarter.git my-local-repository
        Cloning into 'my-local-repository'...
        remote: Enumerating objects: 529, done.
        remote: Counting objects: 100% (148/148), done.
        remote: Compressing objects: 100% (86/86), done.
        Receiving objects:  93% (492/529)used 84 (delta 62), pack-reused 381
        Receiving objects: 100% (529/529), 159.30 KiB | 2.24 MiB/s, done.
        Resolving deltas: 100% (325/325), done.
        ```

1. Change directory into local repository directory:  
    `Set-Location .\my-local-repository\`
    ```
    PS C:\Users\Bruce\Programming> Set-Location .\my-local-repository\
    PS C:\Users\Bruce\Programming\my-local-repository>
    ```

1. Verify directory contents:  
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
        -a---          2022-06-21    09:27          35823 LICENSE
        -a---          2022-06-21    09:27            708 manage.py
        -a---          2022-06-21    09:27            260 Pipfile
        -a---          2022-06-21    09:27           4299 Pipfile.lock
        -a---          2022-06-21    09:27            106 Procfile
        -a---          2022-06-21    09:27           2405 README.md
        ```

1. Verify current remote repository. `origin` is the local name for the https://github.com/brucestull/DjangoCustomUserStarter.git remote:  
    `git remote -v`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> git remote -v
        origin  https://github.com/brucestull/DjangoCustomUserStarter.git (fetch)
        origin  https://github.com/brucestull/DjangoCustomUserStarter.git (push)
        ```

1. Remove git remote repository links for `origin` repository (`origin` is currently mapped to https://github.com/brucestull/DjangoCustomUserStarter.git as noted above) so user can push code to their own repository:  
    `git remote remove origin`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> git remote remove origin
        PS C:\Users\Bruce\Programming\my-local-repository>
        ```

1. Verify there is no current remote repository:  
    `git remote -v`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> git remote -v
        PS C:\Users\Bruce\Programming\my-local-repository>
        ```

1. [Create Empty Remote GitHub Repository and Push Existing Application](create_empty_remote_repo_push_existing_application.md)


## Links:
[README.md](../README.md)