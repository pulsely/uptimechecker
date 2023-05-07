"""
Django settings for uptimechecker project.

Try not to change settings in this file, instead, change at the settings_customized.py file
When you need to upgrade, just do a "git pull origin" from Github.

The settings_customized.py is not added to git, and should merge nicely.

"""

from pathlib import Path
from distutils.util import strtobool
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
if not SECRET_KEY:
    # Raise an exception, if unable to load .env
    raise Exception("Sorry, unable to read configuration.")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(config('DEBUG')))

_allowed_hosts = config("ALLOWED_HOSTS") #os.getenv("ALLOWED_HOSTS", ".localhost,127.0.0.1,[::1]")
ALLOWED_HOSTS = list(map(str.strip, _allowed_hosts.split(",")))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'landing',
    'uptimecheckcore',
    'uptimebot',

    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uptimechecker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'src/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'uptimechecker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'src/static')

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'uptimecheckcore.User'

LOGIN_URL= '/login/'
LOGIN_REDIRECT_URL='/accounts/'
URL_POST_SIGNIN = "panel:index"


# Uptime Checker Defaults
DEFAULT_USER_AGENT = config("DEFAULT_USER_AGENT") #os.getenv("DEFAULT_USER_AGENT", "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15")
DEFAULT_PERIODIC_MINUTES = int(config("DEFAULT_PERIODIC_MINUTES")) #os.getenv("DEFAULT_PERIODIC_TIME", 15)
DEFAULT_ADD_RANDOMNESS = bool(strtobool(config('DEFAULT_ADD_RANDOMNESS')))

# E-mail Settings
EMAIL_BACKEND = config("EMAIL_BACKEND")
AWS_SES_REGION_NAME = config("AWS_SES_REGION_NAME")
AWS_SES_REGION_ENDPOINT = config("AWS_SES_REGION_ENDPOINT")
SERVER_EMAIL = config("SERVER_EMAIL")

# Slack
SLACK_TOKEN = config("SLACK_TOKEN")
SLACK_ROOM  = config("SLACK_ROOM")

#
# # Celery settings

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL

CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 5 * 60

# You can change most of the settings at the .env file
# Configurations are available at the "Uptime Checker" github page:
# https://github.com/pulsely/uptimechecker
#
# You can also overwrite the default Django settings file at uptimechecker/settings_customized.py file
if os.path.exists("uptimechecker/settings_customized.py"):
    from .settings_customized import *

