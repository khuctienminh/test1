"""
Django settings for ryokou_taro project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from decouple import config
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!-lb3bvjvs752z&^pp4=#=m=$ku0+(t96=80nan(#j_r#e4v=&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'taro.apps.TaroConfig',
    'accounts.apps.AccountsConfig',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'ryokou_taro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ryokou_taro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTH_USER_MODEL = 'accounts.CustomUser'

# ロギング設定
LOGGING = {
    'version': 1,  # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'taro': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

MESSAGE_TAGS = {
    messages.ERROR:'alert alert-danger',
    messages.WARNING:'alert alert-warning',
    messages.SUCCESS:'alert alert-success',
    messages.INFO:'alert alert-info',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ryokou_taro',
        #'USER':os.environ.get('DB_USER'),
        #'PASSWORD':os.environ.get('DB_PASSWORD'),
        'USER':'postgres',
        'PASSWORD':'2035145',
        'HOST':'',
        'PORT':'',
    }
}
#khi up len mang thi phai them cai nay

# import dj_database_url
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別用IDを設定
SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',  # 一般ユーザー用(メールアドレス認証)
    'django.contrib.auth.backends.ModelBackend',  # 管理サイト用(ユーザー名認証)
)

# メールアドレス認証に変更する設定
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = True

# サインアップにメールアドレス確認を挟むよう設定
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

# ログイン/ログアウト後の遷移先を設定
LOGIN_REDIRECT_URL = 'taro:top'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

# ログアウトリンクのクリック一発でログアウトする設定
ACCOUNT_LOGOUT_ON_GET = True

# django-allauthが送信するメールの件名に自動付与される接頭辞をブランクにする設定
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

# デフォルトのメール送信元を設定
DEFAULT_FROM_EMAIL = 'admin@example.com'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'

django_heroku.settings(locals())

# メールサーバーへの接続設定

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = 'tdjangoc@gmail.com'

EMAIL_HOST_PASSWORD = 'test2021C'

EMAIL_USE_TLS = True


# ACCOUNT_FORMS   = { "signup":"taro.forms.UserInfoCreateForm"}