from .base import *

PROPS_DIR = BASE_DIR + "/app/properties/dev/"

SECRET_KEY = 'e=73n&qf0sw*2n)&h&&9r9jmhw@hz@b-ci-d3+4z3(k-lqer27'

DEBUG = True

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eurobracket',
        'USER': 'django',
        'PASSWORD': '`~4=(GQDE4x`q$"s',
        'HOST': 'localhost',
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
            'filename': '/Users/scott/desktop/euro-bracket/eurobracket/eurobracket/logs/eurobracket.log'
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
