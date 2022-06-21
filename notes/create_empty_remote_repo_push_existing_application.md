# Create Empty Remote GitHub Repository and Push Existing Application


## Resources:

* [git syncing - atlassian.com](https://www.atlassian.com/git/tutorials/syncing)

## Process:

1. Create an empty GitHub repository. Use https://github.com/new or Click the "New" button on GitHub user repository page:
    * NOTE: It is critical that this remote be an empty repository so there are no merge conflicts or history conflicts. Ensure that "Add a README.md" is not checked, "Add .gitignore" is set to "None" and "Choose a license" is set to "None". We can change this later if desired.

1. Provide a repository name:
![01_create_empty_repository](https://user-images.githubusercontent.com/47562501/174804053-9d5d8096-ec3d-411e-8c41-e775233a97a3.png)

1. Click "Create repository" button:
![02_click_create_repository_button](https://user-images.githubusercontent.com/47562501/174804077-044af48e-c18b-4f28-9b4c-37f65ded228d.png)

1. Click the copy button for the repository address:
    * Sample repository address:  
    `https://github.com/brucestull/new-remote-repository.git`
![03_click_copy_button_for_git_repo](https://user-images.githubusercontent.com/47562501/174804112-d7683dfc-0f6e-4a71-a6fe-279362a0dcfc.png)

1. Navigate, in terminal, to the applications local repository directory:
    * Sample location:  
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming\my-new-app-repository
        ```

1. Verify there are no remote repositories configured:  
`git remote -v`  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> git remote -v
        ```

1. Add connection of our local repository to the remote repository (https://github.com/brucestull/new-remote-repository.git) we created above. We are using the standard 'origin' name for the remote repository:  
    `git remote add origin https://github.com/brucestull/new-remote-repository.git`  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> git remote add origin https://github.com/brucestull/new-remote-repository.git
        ```

1. Verify the remote repository is added. We should now have our own GitHub remote which has a local name of "origin":  
`git remote -v`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> git remote -v
        origin  https://github.com/brucestull/new-remote-repository.git (fetch)
        origin  https://github.com/brucestull/new-remote-repository.git (push)
        ```

1. Push the contents of our local repository to our GitHub remote repository. The "push" won't work since we need to set upstream branch:  
`git push`  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> git push
        fatal: The current branch main has no upstream branch.
        To push the current branch and set the remote as upstream, use

            git push --set-upstream origin main
        ```

1. Use the tip from previous command to set upstream. We are setting up our local "main" branch to track with the remote named "origin"s "main" branch. (NOTE THE FINAL LINE: "branch 'main' set up to track 'origin/main'"):  
    `git push --set-upstream origin main`  
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> git push --set-upstream origin main
        Enumerating objects: 408, done.
        Counting objects: 100% (408/408), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (171/171), done.
        Writing objects: 100% (408/408), 138.37 KiB | 69.18 MiB/s, done.
        Total 408 (delta 235), reused 404 (delta 232), pack-reused 0
        remote: Resolving deltas: 100% (235/235), done.
        To https://github.com/brucestull/new-remote-repository.git
        * [new branch]      main -> main
        branch 'main' set up to track 'origin/main'.
        ```

1. Check that the application's code appears on remote GitHub repository:
    * Sample repository:  
        `https://github.com/brucestull/new-remote-repository`

1. User now has the Django Custom User Starter local repository connected to their own remote on GitHub.

1. [Run Application Locally](run_application_locally.md)


## Links:
[README.md](../README.md)
