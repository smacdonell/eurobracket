from .base import *

PROPS_DIR = BASE_DIR + "/app/properties/live/"

SECRET_KEY = 'e=73n&qf0sw*2n)&h&&9r9jmhw@hz@b-ci-d3+4z3(k-lqer27'

ALLOWED_HOSTS = [
    'localhost',
    'scottify.app',
    '127.0.0.1:8000',
    '127.0.0.1',
    'https://www.scottify.app'
]

DEBUG = False

SECURE_HSTS_SECONDS = 300
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = '.scottify.app'
CSRF_TRUSTED_ORIGINS=[
    'www.scottify.app',
    'scottify.app'
]

STATICFILES_DIRS=[
    '/var/www/www'
]
STATIC_ROOT = '/var/www/www/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eurobracket',
        'USER': 'django',
        'PASSWORD': '`~4=(GQDE4x`q$"s',
        'HOST': 'eurobracket2.ca9raojju2aa.us-east-2.rds.amazonaws.com',
        'PORT': '5432'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'when': 'midnight',
            'filename': '/home/scott/app/eurobracket/eurobracket/eurobracket/logs/eurobracket.log'
        },
    },
    'loggers': {
        'eurobracket': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
