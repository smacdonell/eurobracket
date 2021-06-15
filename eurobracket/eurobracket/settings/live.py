from .base import *

PROPS_DIR = BASE_DIR + "/app/properties/live/"

ALLOWED_HOSTS = [
    'https://www.scottify.app'
]

DEBUG = False

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
            'filename': '/home/eurobracket/app/logs/eurobracket.log'
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
