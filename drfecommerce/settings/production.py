from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com']

# Production database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production_db',
        'USER': 'production_user',
        'PASSWORD': 'production_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Security settings for production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
