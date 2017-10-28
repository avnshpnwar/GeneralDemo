from os.path import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_LOG_LEVEL='DEBUG'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'debugfile': {
            'level': APP_LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR,'logs/debug.log'),
            'maxBytes': 1024*1024, #1 MB
            'backupCount': 5,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['debugfile'],
            'propagate': True,
            'level':'ERROR',
        },
        'GeneralDemo': {
            'handlers': ['debugfile',],
            'propagate': True,
            'level': APP_LOG_LEVEL,
        },
        'Auth': {
            'handlers': ['debugfile',],
            'propagate': True,
            'level': APP_LOG_LEVEL,
        },
        'UserHome': {
            'handlers': ['debugfile',],
            'propagate': True,
            'level': APP_LOG_LEVEL,
        },
    }
}