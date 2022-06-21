# Create Empty Remote GitHub Repository and Push Existing Application


## Resources:

* [git syncing - atlassian.com](https://www.atlassian.com/git/tutorials/syncing)

## Process:

1. Create an empty GitHug repository:
    * NOTE: It is critical that this remote be an empty repository so there are no merge conflicts or history conflicts. Ensure that "Add a README.md" is not checked, "Add .gitignore" is set to "None" and "Choose a license" is set to "None". We can change this later if desired.
    * Sample repository name and URL:  
        * Repository name:  
        `user-created-repository`  
        * Repository URL:  
        `https://github.com/brucestull/user-created-repository.git`  

1. Click the copy button for the repository URL:
    * Sample URL:  
    `https://github.com/brucestull/user-created-repository.git`

1. Navigate, in terminal, to the applications local repository directory:
    * Sample location:  
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive
        ```

1. Verify the only remote repository is the one for Heroku:  
    `git remote -v`  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> git remote -v
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (fetch)
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (push)
        ```

1. Add connection of our local repository to the remote repository (https://github.com/brucestull/user-created-repository.git) we created above. We are using the standard 'origin' name for the remote repository:  
    `git remote add origin https://github.com/brucestull/user-created-repository.git`  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> git remote add origin https://github.com/brucestull/user-created-repository.git
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive>
        ```

1. Verify the remote repository is added. We should now have the "heroku" named remote and our own GitHub "origin" named remote:  
    `git remote -v`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> git remote -v
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (fetch)
        heroku  https://git.heroku.com/totally-new-heroku-app-name.git (push)
        origin  https://github.com/brucestull/user-created-repository.git (fetch)
        origin  https://github.com/brucestull/user-created-repository.git (push)
        ```

1. Push the contents of our local repository to our GitHub remote repository. The "push" won't work since we need to set upstream branch:  
    `git push`  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> git push
        fatal: The current branch main has no upstream branch.
        To push the current branch and set the remote as upstream, use

            git push --set-upstream origin main
        ```

1. Use the tip from previous command to set upstream. We are setting up our local "main" branch to track with the remote named "origin"s "main" branch. (NOTE THE FINAL LINE: "branch 'main' set up to track 'origin/main'"):  
    `git push --set-upstream origin main`  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> git push --set-upstream origin main
        Enumerating objects: 296, done.
        Counting objects: 100% (296/296), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (133/133), done.
        Writing objects: 100% (296/296), 106.83 KiB | 106.83 MiB/s, done.
        Total 296 (delta 165), reused 283 (delta 158), pack-reused 0
        remote: Resolving deltas: 100% (165/165), done.
        To https://github.com/brucestull/user-created-repository.git
        * [new branch]      main -> main
        branch 'main' set up to track 'origin/main'.
        ```

1. Check that the application's code appears on remote GitHub repository:
    * Sample repository:  
        `https://github.com/brucestull/user-created-repository`

1. User now has the Django Custom User Starter local repository connected to their own remote on GitHub.

1. [Run Application Locally](run_application_locally.md)


## Links:
[README.md](../README.md)