import os
import socket

PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = '0a^qwru!y#_(yf__1)etdzo)7e0rro^k*y7q1i9jvp=b3e9^z#'

HOSTNAME = socket.gethostname()
PRODUCTION_SERVERS = ['code-latte.com']

LIVEHOST = HOSTNAME in PRODUCTION_SERVERS

TEMPLATE_DEBUG = DEBUG = not LIVEHOST

if not LIVEHOST:
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    ADMIN_MEDIA_PREFIX = '/static/admin/'
else:
    MEDIA_URL = 'http://cdn.' + HOSTNAME + '/sia/media/'
    STATIC_URL = 'http://cdn.' + HOSTNAME + '/sia/static/'
    ADMIN_MEDIA_PREFIX = 'http://cdn.' + HOSTNAME + '/sia/static/admin/'
    # SITE_ID = 2

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'sia/static/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ADMINS = (
    ('Benny', 'benny.christanto@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    # ---
    'suit',

    # ---
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ---
    'south',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sia.urls'

WSGI_APPLICATION = 'sia.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sia.db.sqlite3'),
    }
}

LANGUAGE_CODE = 'id-id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Sistem Informasi Akademik'
}
