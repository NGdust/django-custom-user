from .base import *

INSTALLED_APPS += 'drf_yasg',
SWAGGER_BASE_URL = os.environ.get('SWAGGER_BASE_URL')

ROOT_URLCONF = 'settings.urls.dev'