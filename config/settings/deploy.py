from .base import *


def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

SECRET_KEY = read_secret('DJANGO_SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': read_secret("POSTGRES_DB"),
        'USER': read_secret("POSTGRES_USER"),
        'PASSWORD': read_secret("POSTGRES_PASSWORD"),
        'HOST': 'postgresdb',
        'PORT': '5432',
    }
}
