"""
Django settings for project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'E#%v02dqcaj23ff#P6k$j88333mbdvvXX27oxgr^57gkgms7&y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['']

TOKEN = ''

BASE_ADMIN_PATH = 'https://'

WEBHOOK_PATH = TOKEN[-6:]
WEBHOOK_URL = f'{BASE_ADMIN_PATH}/{WEBHOOK_PATH}'
PAYMENT_PATH = 'payment_23ni24noan1ms9n4jllfgiwfugw9afg3gaf78wg320'
PAYMENT_URL = f'{BASE_ADMIN_PATH}/{PAYMENT_PATH}'


ADMINS_ = []
DEVS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'admin_reorder',
    'preferences',

    'bot',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 'preferences.context_processors.preferences_cp',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

GDAL_LIBRARY_PATH = '/usr/local/bin/gdal'


ADMIN_REORDER = [
    {
        'app': 'bot',
        'label': 'Information',
        'models': [
            {
                'label': '👳🏻‍♀ Users',
                'model': 'bot.User'
            },
            {
                'label': '📜 Logs',
                'model': 'bot.Log'
            },
            {
                'label': '💵 Orders',
                'model': 'bot.Order'
            },
            {
                'label': '💰 Payments',
                'model': 'bot.Payment'
            },
        ]
    },
    {
        'app': 'bot',
        'label': 'Filling',
        'models': [
            {
                'label': '🌎 Countries',
                'model': 'bot.Country'
            },
            {
                'label': '🛒 Shops',
                'model': 'bot.Shop'
            },
            {
                'label': '❓ Questions',
                'model': 'bot.Question'
            },
            {
                'label': '⚙️ Settings',
                'model': 'bot.Settings'
            },
            {
                'label': '📝 Texts',
                'model': 'bot.Texts'
            },
        ]
    },
    {
        'app': 'bot',
        'label': 'Messaging',
        'models': [
            {
                'label': '📬 Posts',
                'model': 'bot.Post'
            },
        ]
    },
]