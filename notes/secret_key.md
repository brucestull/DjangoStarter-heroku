# `SECRET_KEY` and Environment Variable Concepts

## Pertinent Code Snippets

* `development.py`:

```python
SECRET_KEY = os.environ.get('SECRET_KEY', "mm8cx0al6wo$$0hhv3&eevzsst9dbw&(5p$#9k(1rx%e@j+=$l")
```

## `SECRET_KEY` DOES NOT EXIST IN Environment Variables

* `os.environ.get('SECRET_KEY', "mm8cx0al6wo$$0hhv3&eevzsst9dbw&(5p$#9k(1rx%e@j+=$l")` will return the default value, "mm8cx0al6wo$$0hhv3&eevzsst9dbw&(5p$#9k(1rx%e@j+=$l", if the environment variable, `SECRET_KEY`, does not exist.

```bash
PS C:\Users\FlynntKnapp\Programming\DjangoCustomUserStarter-heroku> python manage.py shell
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.conf import settings as s
>>> s.SECRET_KEY
'mm8cx0al6wo$$0hhv3&eevzsst9dbw&(5p$#9k(1rx%e@j+=$l'
>>> quit()
PS C:\Users\FlynntKnapp\Programming\DjangoCustomUserStarter-heroku>
```

## `SECRET_KEY` EXISTS IN Environment Variables

* Computer's Environment Variables contains a value for `SECRET_KEY`:
  * `5f%hxn95)wyv13ei0q#!y5#=5#15(2efk4j$05yl#=^b45^ia@`

```bash
PS C:\Users\FlynntKnapp\Programming\DjangoCustomUserStarter-heroku> python manage.py shell
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.conf import settings as s
>>> s.SECRET_KEY
'5f%hxn95)wyv13ei0q#!y5#=5#15(2efk4j$05yl#=^b45^ia@'
>>> quit()
PS C:\Users\FlynntKnapp\Programming\DjangoCustomUserStarter-heroku>
```
