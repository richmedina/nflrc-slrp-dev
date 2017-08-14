from .base import *

ALLOWED_HOSTS += ['clt.developers.edu']

SECRET_KEY = os.environ['SECRET_KEY']

# INSTALLED_APPS += (
#     'debug_toolbar',
# )

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

STATIC_ROOT = '/Library/WebServer/Documents/static/nflrcllt'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nflrc-llt-dev-db',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

GOOGLE_RECAPTCHA_SECRET_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_KEY']