import os

# Set the default settings module
environment = os.getenv('DJANGO_ENV', 'local')  # Default to 'local'

if environment == 'production':
    from .production import *
else:
    from .local import *
