from .base import *

DEBUG = True
ALLOWED_HOSTS = ['https://secure-basin-29081.herokuapp.com/']
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'hooria654321',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

STRIPE_PUBLIC_KEY = 'pk_test_cR7bvsieZTgD2oDp5pFIe4sg00XYyANA59'
STRIPE_SECRET_KEY = 'sk_test_NMSZF5w3P2ihIBJAosiViqE200RuREs2WB'
