from .base import *

def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()


SECRET_KEY = read_secret("DJANGO_SECRET_KEY")

DEBUG = False

# * 로 하면 모든 PC에서 접근 가능하다. 
# 회사 내부에서만 사용하려면 내부 컴퓨터 IP 주소를 넣어주면 된다.
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': read_secret("POSTGRES_DB"),
        'USER': read_secret("POSTGRES_USER"),
        'PASSWORD': read_secret("POSTGRES_PASSWORD"),
        'HOST': 'postgresdb',
        # docker-container 끼리는 보통 5432 끼리 통신한다.
        'PORT': '5432',
    }
}