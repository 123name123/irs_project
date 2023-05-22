import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-)_39wb7hv+^kdp!s&%koxs0+k&28v$myl$*2ai@r$(v59+8eju')

DEBUG = int(os.getenv('DEBUG', 1))

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
CORS_URLS_REGEX = r'^/api/.*$'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'django_filters',
    'users.apps.UsersConfig',
    'shop.apps.ShopConfig',
    'api.apps.ApiConfig',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {

    'default': {
        'ENGINE': os.environ.get('DB_ENGINE_DEFAULT', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('POSTGRES_DB_DEFAULT', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER_DEFAULT', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD_DEFAULT', 'postgres'),
        'HOST': os.environ.get('DB_HOST_DEFAULT', 'localhost'),
        'PORT': os.environ.get('DB_PORT_DEFAULT', '5432'),
    },

    "shop_db": {
        'ENGINE': os.environ.get('DB_ENGINE_SHOP', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('POSTGRES_DB_SHOP', 'shops01'),
        'USER': os.environ.get('POSTGRES_USER_SHOP', 'ushops01'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD_SHOP', 'HSEP@ssword2022'),
        'HOST': os.environ.get('DB_HOST_SHOP', '84.201.135.211'),
        'PORT': os.environ.get('DB_PORT_SHOP', '5430'),
    },

}

DATABASE_ROUTERS = ['users.models.MainRouter']

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


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static_files/'  # потому что static путь занят реактом
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.CustomUser"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
DJOSER = {
    'HIDE_USERS': False,
    'PERMISSIONS': {
        'user': ['rest_framework.permissions.AllowAny'],
        'user_list': ['rest_framework.permissions.AllowAny'],
    },
}
