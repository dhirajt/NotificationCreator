"""Production settings and globals."""

from __future__ import absolute_import

from .base import *

import os


########## HOST CONFIGURATION
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = [PROJECT_DOMAIN, '.herokuapp.com', 'localhost', '127.0.0.1']
########## END HOST CONFIGURATION


########## SECRET CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.environ['SECRET_KEY']
########## END SECRET CONFIGURATION


########## EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = '%s Team <contact@%s>' % (PROJECT_NAME, PROJECT_DOMAIN)

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.gmail.com'

# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 587

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}
########## END DATABASE CONFIGURATION


########## TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
########## END TEMPLATE CONFIGURATION


########## SECURITY CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/middleware/#django.middleware.security.SecurityMiddleware
# MIDDLEWARE_CLASSES += (
#     'django.middleware.security.SecurityMiddleware',
# )

# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECURE_PROXY_SSL_HEADER
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# # Use this setting if SSL is being served through CloudFlare proxy
# SECURE_PROXY_SSL_HEADER = ('HTTP_CF_VISITOR', '{"scheme":"https"}',)

# # Set this to 30 seconds and then to 31536000 when you can prove it works
# SECURE_HSTS_SECONDS = 30
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# X_FRAME_OPTIONS = 'DENY'
########## END SECURITY CONFIGURATION

