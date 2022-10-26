"""
Django settings for likeestampa project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_&%r6!rao1dl+&wkye8f9bu#mc7gr#^$bn!6^@_5oiurzgkw1j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # TERCEIROS
    'cloudinary',
    'localflavor',
    'mathfilters',
    'widget_tweaks',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'anymail',
    'fontawesomefree',

    # LOCAL
    'apps.core',
    'apps.catalogo',
    'apps.checkout',
    'apps.evento',
    'apps.pagamento',
    'apps.pedido',
    'apps.seller',
    'apps.usuario',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'likeestampa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'likeestampa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "likeestampa",
#         "USER": "likeestampa",
#         "PASSWORD": "likeestampa",
#         "HOST": "localhost",
#         "PORT": 5432,
#     }
# }

# # Update database configuration with $DATABASE_URL.
# DATABASES['default'].update(dj_database_url.config())

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
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

# Sessions
# SESSION_EXPIRE_AT_BROWSER_CLOSE=True
# SESSION_COOKIE_AGE = 20


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CLOUDINARY CONFIGS
CLOUDINARY = {
    'cloud_name': os.environ.get('CLOUDINARY_CLOUD_NAME', 'leonardocintra'),
    'api_key': os.environ.get('CLOUDINARY_API_KEY', '182946961533113'),
    'api_secret': os.environ.get('CLOUDINARY_API_SECRET', 'LAIVTLNHtG5x-TTdUmHgaE3CnsM'),
}


# MERCADO PAGO
MERCADO_PAGO_PUBLIC_KEY = 'TEST-1f3bd514-5066-47ba-bc5a-cc59eedfdf64'
MERCADO_PAGO_PRIVATE_KEY = 'TEST-7112055085058773-060901-5d4a8146dcccf6e2216931dc77d834fb-4990865'

# MELHOR ENVIO
MELHOR_ENVIO_TOKEN = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjZlYTAxNmNiMDc3ZGQ1MTZmYjIxN2VjZDFmMDJhZWEyYzEzNzViZjQxMDViNjRiMDg2MzZjOGYzYjFjYTU0NTQ5Mzc4MDlkYWYwMjAzOGVhIn0.eyJhdWQiOiI5NTYiLCJqdGkiOiI2ZWEwMTZjYjA3N2RkNTE2ZmIyMTdlY2QxZjAyYWVhMmMxMzc1YmY0MTA1YjY0YjA4NjM2YzhmM2IxY2E1NDU0OTM3ODA5ZGFmMDIwMzhlYSIsImlhdCI6MTYyMzk0NjE3NiwibmJmIjoxNjIzOTQ2MTc2LCJleHAiOjE2NTU0ODIxNzYsInN1YiI6ImRlNjhmZDdmLWUyNDQtNDQyOS1hZjdlLTZiNWVhMTlmMmEwMCIsInNjb3BlcyI6WyJjYXJ0LXJlYWQiLCJjYXJ0LXdyaXRlIiwiY29tcGFuaWVzLXJlYWQiLCJjb21wYW5pZXMtd3JpdGUiLCJjb3Vwb25zLXJlYWQiLCJjb3Vwb25zLXdyaXRlIiwibm90aWZpY2F0aW9ucy1yZWFkIiwib3JkZXJzLXJlYWQiLCJwcm9kdWN0cy1yZWFkIiwicHJvZHVjdHMtZGVzdHJveSIsInByb2R1Y3RzLXdyaXRlIiwicHVyY2hhc2VzLXJlYWQiLCJzaGlwcGluZy1jYWxjdWxhdGUiLCJzaGlwcGluZy1jYW5jZWwiLCJzaGlwcGluZy1jaGVja291dCIsInNoaXBwaW5nLWNvbXBhbmllcyIsInNoaXBwaW5nLWdlbmVyYXRlIiwic2hpcHBpbmctcHJldmlldyIsInNoaXBwaW5nLXByaW50Iiwic2hpcHBpbmctc2hhcmUiLCJzaGlwcGluZy10cmFja2luZyIsImVjb21tZXJjZS1zaGlwcGluZyIsInRyYW5zYWN0aW9ucy1yZWFkIiwidXNlcnMtcmVhZCIsInVzZXJzLXdyaXRlIiwid2ViaG9va3MtcmVhZCIsIndlYmhvb2tzLXdyaXRlIl19.G04FCla_B7ZcvjEjVZYtLQ57xTZK_Xju2mKrO7jLPv5Oas1a_uiy6-KpMBfaU8tq8MYvHqb7B0prjnZdzG_RIk_RPQizWIxPOfLwx9QYxphRofq551tkJRuPVUK1nPyUtQ5WInBSmMtETQ42ylewpjyx3tuHzE8ekP1ELqfaR4JWgoFpw21jX1p6A990KTUqHzd_dkzB6gdns9YLWjFwO4M85jZ9I8oycicsB4kXuPtIXEXMI-65xJI5_pVTooJY0ZaR-eIrPbz5Ky7Aqow6q52ze3ZVy3R2__FDs_yvMbEME4ftefjNMlUxxhtrymlr0RYMOlY1na89iSo8Vw-eKwaTRWkJzGX1mOFz6Grs8YnVT5McfUmQS_7JwjJP4BxRM-GakvBUOVfXGNIBx5BNLykwgHaKObIGjvKw51sIAvGtmsisfyG9dP2RF_y9TtlscwhZQsa3e0eh1SseOxExgFL0s5I-xadfe1RMI2UFHuPPgryJ-MnX_6IMaWEoMumOiKlODPanEEw5w2wSVXm4JyLgKDlNlkYC1HMBogbZ_G8DfFTmLXOfpnjb5Fa_VkQmUNqGh7jRWdOPQNGPaEzgfwVm1ZRwHs07aiHynxBY0qXMayXiKZRd8xLnWqtO9aZVUAM6Y6Oagu8kmI_Mm8cVRjGoh3KcP2nxas9qEVFf9kE'
MELHOR_ENVIO_BASE_URL = "https://sandbox.melhorenvio.com.br"

MAXIMO_ITENS_CARRINHO = 10


# Django All Auth
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
ACCOUNT_SIGNUP_FORM_CLASS = 'apps.usuario.forms.SignupForm'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_REDIRECT_URL = "/usuario/"


# Django Crispy Form
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# DIMONA
DIMONA_KEY = 'f9bb66ac5feaebd7b97206198866a898'

# TELEGRAM
TELEGRAM_TOKEN = '508627689:AAEuLPKs-EhrjrYGnz60bnYNZqakf6HJxc0'
