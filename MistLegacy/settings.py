"""
Django settings for MistLegacy project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y9xucupzvxm1jmi5g=88r45ifi7r6_3*qqttiq$42crwjr@t94'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['nacros.eu.pythonanywhere.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'front.apps.FrontConfig',
    'djgeojson',
    'leaflet',
    'easy_thumbnails',
    'filer',
    'mptt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MistLegacy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'front.context_processor.geojson_locations',
                'front.context_processor.geojson_regions'
            ],
        },
    },
]

WSGI_APPLICATION = 'MistLegacy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
        'TIMEOUT': 86400
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/mldb/static'
MEDIA_ROOT = '/mldb/media'
MEDIA_URL = '/media/'

MODELTRANSLATION_ENABLE_FALLBACKS = False
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
)
LOCALE_PATHS = [
    '/mldb/locale',
    'C:/Users/Fabrice/PycharmProjects/MistLegacy/locale',
]

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-5.0, -57.0),
    'DEFAULT_ZOOM': 5,
    'MIN_ZOOM': 5,
    'MAX_ZOOM': 8,
    'TILES': '/static/map/{z}/{y}/{x}.jpg',
    'ATTRIBUTION_PREFIX': '&copy; Virtys',
    'SCALE': None,
    'MINIMAP': False,
    'PLUGINS': {
        'MousePosition': {
            'css': '/static/assets/mldb/map/L.Control.MousePosition.css',
            'js': 'assets/mldb/map/L.Control.MousePosition.js',
            'auto-include': False,
        },
        'FullScreen': {
            'css': 'https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/leaflet.fullscreen.css',
            'js': 'https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/Leaflet.fullscreen.min.js',
            'auto-include': True,
        },
    }
}

if os.path.exists(r"c:\python37"):
    os.environ['GDAL_DATA'] = r"C:\Python37\Lib\site-packages\osgeo\data\gdal"
    os.environ['PROJ_LIB'] = r"C:\Python37\Lib\site-packages\osgeo\data\proj"
    os.environ['PATH'] = r"C:\Python37\Lib\site-packages\osgeo" + ";" + os.environ['PATH']
    GDAL_LIBRARY_PATH = r'C:\Python37\Lib\site-packages\osgeo\gdal302.dll'
    if os.path.exists(r"C:\Users\cantin-f"):
        MEDIA_ROOT = r'C:\Users\cantin-f\PycharmProjects\mldb\media'
    else:
        MEDIA_ROOT = r'C:\Users\Fabrice\PycharmProjects\MistLegacy\media'
