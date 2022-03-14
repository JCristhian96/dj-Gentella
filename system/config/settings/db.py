from .base import BASE_DIR, os


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child("config", 'db.sqlite3'),
    }
}