# Clone DjangoCustomUserStarter Repository

## Resources:

## Process:
1. Get remote repository URL:
    * https://github.com/brucestull/DjangoCustomUserStarter-archive
1. Open terminal:
    * Sample location:
        ```
        C:\Users\Bruce
        ```
1. Change directory into parent directory where repository will be located:
`Set-Location .\Programming\`
    * Sample output:
        ```
        PS C:\Users\Bruce> Set-Location .\Programming\
        PS C:\Users\Bruce\Programming>
        ```
1. Clone remote repository into current directory:
`git clone https://github.com/brucestull/DjangoCustomUserStarter-archive`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming> git clone https://github.com/brucestull/DjangoCustomUserStarter-archive
        Cloning into 'DjangoCustomUserStarter-archive'...
        remote: Enumerating objects: 345, done.
        remote: Counting objects: 100% (45/45), done.
        remote: Compressing objects: 100% (34/34), done.
        Receiving objects: 100% (345/345), 112.60 KiB | 1.68 MiB/s, done.00

        Resolving deltas: 100% (196/196), done.
        ```
1. Change directory into local repository directory:
`Set-Location .\DjangoCustomUserStarter-archive\`
1. Verify directory contents:
`Get-ChildItem`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> Get-ChildItem

            Directory: C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d----          2022-06-20    09:04                my_current_project
        d----          2022-06-20    09:04                notes
        d----          2022-06-20    09:04                templates
        d----          2022-06-20    09:04                users
        -a---          2022-06-20    09:04           1470 .gitignore
        -a---          2022-06-20    09:04          35823 LICENSE
        -a---          2022-06-20    09:04            708 manage.py
        -a---          2022-06-20    09:04            244 Pipfile
        -a---          2022-06-20    09:04           9066 Pipfile.lock
        -a---          2022-06-20    09:04            106 Procfile
        -a---          2022-06-20    09:04           1800 README.md
        ```
1. RUN-APPLICATION-LOCALLY

## Links:
[README.md](..\README.md)