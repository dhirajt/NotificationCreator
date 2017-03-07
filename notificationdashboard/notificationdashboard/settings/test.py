from __future__ import absolute_import

from .base import *


########## TEST RUNNER CONFIGURATION
# https://github.com/django-nose/django-nose
INSTALLED_APPS += (
)

TEST = DEBUG = True

########## END TEST RUNNER CONFIGURATION


########## IN-MEMORY TEST DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'test.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
########## END IN-MEMORY TEST DATABASE


########## EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
########## END EMAIL CONFIGURATION

