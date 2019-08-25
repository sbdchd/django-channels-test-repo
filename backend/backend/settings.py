import os

import dj_database_url
from django.conf import global_settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.getenv("DEBUG") == "1"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+p(5+wb+(l2$@iv!1*3=5xnrw2gvi+l$kuo9s7=u6*)ri4v6as"

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "core.apps.CoreConfig",
    "rest_framework",
    "django.contrib.sites",
    "django.contrib.postgres",
    "channels",
]

WSGI_APPLICATION = "backend.wsgi.application"

ASGI_APPLICATION = "backend.routing.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
        # "BACKEND": "channels_redis.core.RedisChannelLayer",
        # "CONFIG": {
        #     "hosts": [os.environ["REDIS_CHANNEL_URL"]]
        # },
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("core.permissions.DisallowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

# https://stackoverflow.com/questions/25468676/django-sites-model-what-is-and-why-is-site-id-1#25468782
SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.http.ConditionalGetMiddleware",
]


AUTH_USER_MODEL = "core.MyUser"

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"}
]

# use fast password hasher for testing
if DEBUG:
    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",
        *global_settings.PASSWORD_HASHERS,
    ]

# system check framework
SILENCED_SYSTEM_CHECKS = [
    # We don't use messages and sessions in our user facing app. The admin page works fine without these too.
    # (admin.E406) 'django.contrib.messages' must be in INSTALLED_APPS in order to use the admin application.
    "admin.E406",
    # (admin.E407) 'django.contrib.sessions' must be in INSTALLED_APPS in order to use the admin application.
    "admin.E407",
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "/var/app/static"
