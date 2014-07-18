# Django 1.6

#Imports from Python & django
from datetime   import timedelta
from os         import path
import os
import dj_database_url
import psycopg2

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '_pxut=d2%nj*kc#(jq!iu145!4l17byaf_*0agzm1^sl0$m_9q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'manager.urls'

WSGI_APPLICATION = 'manager.wsgi.application'


# Database
if not os.environ.has_key('HEROKU_POSTGRESQL_ONYX_URL'):
    os.environ['HEROKU_POSTGRESQL_ONYX_URL'] = 'postgres://db_usr:db_pwd@localhost/db_db'

DATABASES = {'default': dj_database_url.config(default=os.environ['HEROKU_POSTGRESQL_ONYX_URL'])}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG404 = True
# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Access to templates (Html files)
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

PROJECT_ROOT = path.dirname(path.abspath(__file__))

# Acces to media files
MEDIA_ROOT = PROJECT_ROOT + '/media/'
MEDIA_URL = '/media/'