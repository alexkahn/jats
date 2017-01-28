from .base import *  # noqa


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

THIRD_PARTY = THIRD_PARTY + ['django_extensions', ]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + APPS
