import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in productieon!
DEBUG = False

ALLOWED_HOSTS = ['31.131.24.99']

CACHE_MIDDLEWARE_SECONDS = 21 * 60

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sedb',
        'USER': 'se',
        'PASSWORD': os.environ["SE_DB_PASSWORD"],
        'HOST': '31.131.24.99',
        'PORT': '5432',
    }
}

CACHES = {
      'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': '31.131.24.99:11211',
        'TIMEOUT': 21 * 60,
        'BINARY': True,
        'OPTIONS': {
            'tcp_nodelay': True
        }
      }
    }

#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = '/tmp/app-messages' # change this to a proper location

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'