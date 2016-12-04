import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in productieon!
DEBUG = False

ALLOWED_HOSTS = ['31.131.24.99']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	    'LOCATION': 'localhost:11211',
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
	    'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': None,
        'BINARY': True,
        'OPTIONS': {
            'tcp_nodelay': True,
            'no_block': True,
        }
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = '/tmp/app-messages' # change this to a proper location

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'