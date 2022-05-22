## Install `pipenv`:  

### Assumptions

* `python` is already installed.

### Notes

* Replace `python`, below, with whatever command is used on your system to invoke python (Examples: py, python3, etc).

### Process

1. Verify `python` is installed:  
`python --version`
    * Sample output:  
        ```
        Python 3.10.4
        ```

1. Verify `pip` is installed:  
`pip --version`
    * Sample output:
        ```
        pip 22.1 from C:\Users\User\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
        ```

1. Inspect currently installed packages:  
`pip list`
    * Sample output:  
        ```
        Package    Version
        ---------- -------
        pip        22.1
        setuptools 58.1.0
        ```

1. Install `pipenv`:  
`pip install pipenv`
    * Sample output:
        * NOTE: This output indicates 'Using cached `package_name`' in some places since I've previously had some of these packages installed.
            ```
            PS C:\Users\User\Programming\DjangoCustomUserStarter> pip install pipenv
            Collecting pipenv
            Using cached pipenv-2022.5.2-py2.py3-none-any.whl (3.9 MB)
            Collecting certifi
            Using cached certifi-2022.5.18.1-py3-none-any.whl (155 kB)
            Collecting virtualenv-clone>=0.2.5
            Using cached virtualenv_clone-0.5.7-py3-none-any.whl (6.6 kB)
            Requirement already satisfied: pip>=22.0.4 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pipenv) (22.1)
            Collecting virtualenv
            Using cached virtualenv-20.14.1-py2.py3-none-any.whl (8.8 MB)
            Requirement already satisfied: setuptools>=36.2.1 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pipenv) (58.1.0)
            Collecting platformdirs<3,>=2
            Using cached platformdirs-2.5.2-py3-none-any.whl (14 kB)
            Collecting distlib<1,>=0.3.1
            Using cached distlib-0.3.4-py2.py3-none-any.whl (461 kB)
            Collecting filelock<4,>=3.2
            Using cached filelock-3.7.0-py3-none-any.whl (10 kB)
            Collecting six<2,>=1.9.0
            Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
            Installing collected packages: distlib, virtualenv-clone, six, platformdirs, filelock, certifi, virtualenv, pipenv
            Successfully installed certifi-2022.5.18.1 distlib-0.3.4 filelock-3.7.0 pipenv-2022.5.2 platformdirs-2.5.2 six-1.16.0 virtualenv-20.14.1 virtualenv-clone-0.5.7
            ```
        * Output on install without cached packages:  
            ```
            PS C:\Users\User\Programming\DjangoCustomUserStarter-template> pip install pipenv
            Collecting pipenv
            Downloading pipenv-2022.5.2-py2.py3-none-any.whl (3.9 MB)
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 16.8 MB/s eta 0:00:00
            Collecting certifi
            Downloading certifi-2022.5.18.1-py3-none-any.whl (155 kB)
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.2/155.2 KB ? eta 0:00:00
            Requirement already satisfied: setuptools>=36.2.1 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pipenv) (58.1.0)
            Requirement already satisfied: pip>=22.0.4 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pipenv) (22.0.4)
            Collecting virtualenv
            Downloading virtualenv-20.14.1-py2.py3-none-any.whl (8.8 MB)
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.8/8.8 MB 28.1 MB/s eta 0:00:00
            Collecting virtualenv-clone>=0.2.5
            Downloading virtualenv_clone-0.5.7-py3-none-any.whl (6.6 kB)
            Collecting six<2,>=1.9.0
            Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
            Collecting platformdirs<3,>=2
            Downloading platformdirs-2.5.2-py3-none-any.whl (14 kB)
            Collecting distlib<1,>=0.3.1
            Downloading distlib-0.3.4-py2.py3-none-any.whl (461 kB)
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 461.2/461.2 KB 28.2 MB/s eta 0:00:00
            Collecting filelock<4,>=3.2
            Downloading filelock-3.7.0-py3-none-any.whl (10 kB)
            Installing collected packages: distlib, virtualenv-clone, six, platformdirs, filelock, certifi, virtualenv, pipenv
            Successfully installed certifi-2022.5.18.1 distlib-0.3.4 filelock-3.7.0 pipenv-2022.5.2 platformdirs-2.5.2 six-1.16.0 virtualenv-20.14.1 virtualenv-clone-0.5.7
            WARNING: You are using pip version 22.0.4; however, version 22.1.1 is available.
            You should consider upgrading via the 'C:\Users\User\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip' command.
            PS C:\Users\User\Programming\DjangoCustomUserStarter-template>
            ```

1. Inspect currently installed packages:  
`pip list`  
    * Sample output:
        ```
        Package          Version
        ---------------- -----------
        certifi          2022.5.18.1
        distlib          0.3.4
        filelock         3.7.0
        pip              22.1
        pipenv           2022.5.2
        platformdirs     2.5.2
        setuptools       58.1.0
        six              1.16.0
        virtualenv       20.14.1
        virtualenv-clone 0.5.7
        ```
    * Note that several (about 8) packages were installed in addition to `pipenv`. These are dependencies which `pip` installs automagically.

1. `pipenv` is now installed, proceed to LINK-TO-NEXT-STEP to continue process.
