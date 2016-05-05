import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['31.131.24.99']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sedb',
        'USER': 'se',
        'PASSWORD': os.environ["SE_DB_PASSWORD"],
        'HOST': '31.131.24.99',
        'PORT': '5432',
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = '/tmp/app-messages' # change this to a proper location

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'