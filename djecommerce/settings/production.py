from .base import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ['https://xannys.herokuapp.com/']
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5r8t1k4qt8n1j',
        'USER': 'yqhjetxvgyrwze',
        'PASSWORD': 'eb298ac9258b338a14bbc12d53a9e5fb0d8dfcb6e6e0b0bc4e99fa56939e5d36',
        'HOST': 'ec2-107-21-104-31.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


STRIPE_PUBLIC_KEY = 'pk_test_cR7bvsieZTgD2oDp5pFIe4sg00XYyANA59'
STRIPE_SECRET_KEY = 'sk_test_NMSZF5w3P2ihIBJAosiViqE200RuREs2WB'
