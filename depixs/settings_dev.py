# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# from media_version import get_hg_version

# MEDIA_VERSION = get_hg_version()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '56j-mhs!)b@_ecgyaxplo*2_00%r^(2ossgx=i!-zkvyz9t-vg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# TEMPLATE_DEBUG = True


ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'core.user'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'raven.contrib.django.raven_compat',
    'push_notifications',
    'sekizai',
    'cookielaw',
    'sorl.thumbnail',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'depixs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'depixs.context_processors.general_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'depixs.wsgi.application'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'depixs2',
        'USER': 'root',
        'PASSWORD': 'BuilderSql18',
        'HOST': 'vipasima.customia.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES',storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci",
            'charset': 'utf8',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
TIME_ZONE = 'Europe/Madrid'

LANGUAGE_CODE = 'ES-es'

USE_I18N = True

USE_L10N = False

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

APNS_USE_SANDBOX = True

# GOOGLE_ANALYTICS_ID = 'UA-118890733-1'

API_FACEBOOK_ID = '1517758581607192'

REDIRECT_URI = 'http://192.168.1.49:8000/login/'

NUM_CONVERSATION_TO_DIVIDE_FOR_PERCENT = 30.0  # Num that divides conversations and gets percent
PERCENT_TO_DEPIXS_ON_API_CALL = 30  # Percent that is applied to photo when user called method
MIN_CHARACTERS_TO_DEPIXS = 5  # Number that puts a character limit to chat messages
POINTS_INVITE_DEPIXS = 100  # Number of points that a user wins whenever someone joins Depixs with the invitation link
POINTS_WIN_DEPIXS = 150  # Number of points that a user wins whenever guesses the right user.
POINTS_LOSE_DEPIXS = 25  # Number of points that a user loses whenever guesses the wrong user.

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'ae24ae0254d067'
EMAIL_HOST_PASSWORD = '0b327a68d7703c'
EMAIL_PORT = '2525'
