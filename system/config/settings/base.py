import os
from django.contrib import messages
from django.urls import reverse_lazy
# Terceros
from unipath import Path
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).ancestor(3)
# Secret Keys
load_dotenv(BASE_DIR.child(".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'apps.core',
    'apps.users',
    'apps.products',
)

THRID_PARTY_APPS = (
    'widget_tweaks',    # Add Class to Forms
    'easy_thumbnails',  # Thumbnails
)

INSTALLED_APPS = list(DJANGO_APPS + LOCAL_APPS + THRID_PARTY_APPS)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


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

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Model for User
AUTH_USER_MODEL = 'users.User'


# URLs Login
LOGIN_URL = reverse_lazy('users:login')
LOGOUT_REDIRECT_URL = reverse_lazy("users:login")
LOGIN_REDIRECT_URL = reverse_lazy('index')


# Change class of messages (Tags)
MESSAGE_TAGS = { 
    messages.SUCCESS: 'green',
    messages.ERROR: 'red',
    messages.INFO: 'blue',
    messages.WARNING: 'yellow'
}# blue, red, green, yellow


# Thumbnails Config
THUMBNAIL_ALIASES = {
    '': {
        'thumbnail': {'size': (60, 60), 'crop': 'smart'},
        'thumbnail_mark': {'size': (90, 60), 'crop': 'smart'},
        #'avatar': {'size': (50, 50), 'crop': True},
    },
}
