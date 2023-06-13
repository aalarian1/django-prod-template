# whatto

3erian

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy whatto

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd whatto
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

```
whatto
├─ .dockerignore
├─ .editorconfig
├─ .gitattributes
├─ .github
│  ├─ dependabot.yml
│  └─ workflows
│     └─ ci.yml
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .pylintrc
├─ .readthedocs.yml
├─ README.md
├─ compose
│  ├─ local
│  │  ├─ django
│  │  │  ├─ Dockerfile
│  │  │  ├─ celery
│  │  │  │  ├─ beat
│  │  │  │  │  └─ start
│  │  │  │  ├─ flower
│  │  │  │  │  └─ start
│  │  │  │  └─ worker
│  │  │  │     └─ start
│  │  │  └─ start
│  │  └─ docs
│  │     ├─ Dockerfile
│  │     └─ start
│  └─ production
│     ├─ aws
│     │  ├─ Dockerfile
│     │  └─ maintenance
│     │     ├─ download
│     │     └─ upload
│     ├─ django
│     │  ├─ Dockerfile
│     │  ├─ celery
│     │  │  ├─ beat
│     │  │  │  └─ start
│     │  │  ├─ flower
│     │  │  │  └─ start
│     │  │  └─ worker
│     │  │     └─ start
│     │  ├─ entrypoint
│     │  └─ start
│     ├─ postgres
│     │  ├─ Dockerfile
│     │  └─ maintenance
│     │     ├─ backup
│     │     ├─ backups
│     │     └─ restore
│     └─ traefik
│        ├─ Dockerfile
│        └─ traefik.yml
├─ config
│  ├─ __init__.py
│  ├─ api_router.py
│  ├─ celery_app.py
│  ├─ settings
│  │  ├─ __init__.py
│  │  ├─ base.py
│  │  ├─ local.py
│  │  ├─ production.py
│  │  └─ test.py
│  ├─ urls.py
│  └─ wsgi.py
├─ docs
│  ├─ Makefile
│  ├─ __init__.py
│  ├─ conf.py
│  ├─ howto.rst
│  ├─ index.rst
│  ├─ make.bat
│  └─ users.rst
├─ local.yml
├─ locale
│  └─ README.rst
├─ manage.py
├─ merge_production_dotenvs_in_dotenv.py
├─ production.yml
├─ pytest.ini
├─ requirements
│  ├─ base.txt
│  ├─ local.txt
│  └─ production.txt
├─ setup.cfg
└─ whatto
   ├─ __init__.py
   ├─ conftest.py
   ├─ contrib
   │  ├─ __init__.py
   │  └─ sites
   │     ├─ __init__.py
   │     └─ migrations
   │        ├─ 0001_initial.py
   │        ├─ 0002_alter_domain_unique.py
   │        ├─ 0004_alter_options_ordering_domain.py
   │        └─ __init__.py
   ├─ eat
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  │  └─ __init__.py
   │  ├─ models.py
   │  ├─ serializers.py
   │  ├─ tests.py
   │  └─ views.py
   ├─ static
   │  ├─ css
   │  │  └─ project.css
   │  ├─ fonts
   │  │  └─ .gitkeep
   │  ├─ images
   │  │  └─ favicons
   │  │     └─ favicon.ico
   │  └─ js
   │     └─ project.js
   ├─ templates
   │  ├─ 403.html
   │  ├─ 404.html
   │  ├─ 500.html
   │  ├─ account
   │  │  ├─ account_inactive.html
   │  │  ├─ base.html
   │  │  ├─ email.html
   │  │  ├─ email_confirm.html
   │  │  ├─ login.html
   │  │  ├─ logout.html
   │  │  ├─ password_change.html
   │  │  ├─ password_reset.html
   │  │  ├─ password_reset_done.html
   │  │  ├─ password_reset_from_key.html
   │  │  ├─ password_reset_from_key_done.html
   │  │  ├─ signup.html
   │  │  ├─ signup_closed.html
   │  │  └─ verified_email_required.html
   │  ├─ base.html
   │  ├─ pages
   │  │  ├─ about.html
   │  │  └─ home.html
   │  └─ users
   │     ├─ user_detail.html
   │     └─ user_form.html
   ├─ users
   │  ├─ __init__.py
   │  ├─ adapters.py
   │  ├─ admin.py
   │  ├─ api
   │  │  ├─ serializers.py
   │  │  └─ views.py
   │  ├─ apps.py
   │  ├─ context_processors.py
   │  ├─ forms.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  │  └─ __init__.py
   │  ├─ models.py
   │  ├─ tasks.py
   │  ├─ tests
   │  │  ├─ __init__.py
   │  │  ├─ factories.py
   │  │  ├─ test_admin.py
   │  │  ├─ test_drf_urls.py
   │  │  ├─ test_drf_views.py
   │  │  ├─ test_forms.py
   │  │  ├─ test_models.py
   │  │  ├─ test_tasks.py
   │  │  ├─ test_urls.py
   │  │  └─ test_views.py
   │  ├─ urls.py
   │  └─ views.py
   └─ utils
      ├─ __init__.py
      └─ storages.py

```