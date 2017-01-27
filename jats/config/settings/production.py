from .base import *

DEBUG = False

ALLOWED_HOSTS = ['jats.herokuapp.com']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + APPS

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
