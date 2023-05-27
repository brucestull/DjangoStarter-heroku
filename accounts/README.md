## URL Mappings

# URLs and Views Provided by Django `auth` App

| URL                                  | View Name                        |
| ------------------------------------ | -------------------------------- |
| accounts/login/                      | [name='login']                   |
| accounts/logout/                     | [name='logout']                  |
| accounts/password_change/            | [name='password_change']         |
| accounts/password_change/done/       | [name='password_change_done']    |
| accounts/password_reset/             | [name='password_reset']          |
| accounts/password_reset/done/        | [name='password_reset_done']     |
| accounts/reset/\<uidb64\>/\<token\>/ | [name='password_reset_confirm']  |
| accounts/reset/done/                 | [name='password_reset_complete'] |

## We override the following `View`

`accounts/login/` is mapped to `CustomUserLoginView` instead of `LoginView` provided by Django.

| URL             | View Name      | Our View Class    | Django View Class |
| --------------- | -------------- | ----------------- | ----------------- |
| accounts/login/ | [name='login'] | `CustomUserLoginView` | `LoginView`       |

## NOTE

We don't give the `accounts` app an `app_name` since Django-provided views are not namespaced. And mixing our namespaced urls with Django-provided urls will make url mappings inconsistent in the templates.

If we give `accounts` app an `app_name` of `accounts`:
| View Name                        | URL Name          |
| -------------------------------- | ----------------- |
| [name='login']                   | `accounts:login`  |
| [name='password_reset']          | `password_reset`  |
