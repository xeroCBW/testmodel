"""
Django settings for RestAdm project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime

import djcelery
from corsheaders.defaults import default_headers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+!&#rskr@hrr%@gw0ab&$s5gpg7)qxyigmw_+8ach0@@1nv1+8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_filters',
    # 设置查询过滤器,注意不能大于版本2.0.2
    # 'django_filter',
    'rest_framework.authtoken',
    'debug_toolbar',
    'system',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.check_token_middleware.CheckTokenMiddleware',
    'utils.log_middleware.RequestLogMiddleware',
    # 'utils.disable_csrf_middleware.DisableCSRFCheck',
    # 'utils.ip_block_middleware.IPBlockMiddleWare',
    # debug-tool
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'RestAdm.urls'

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

WSGI_APPLICATION = 'RestAdm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rest_adm',        #数据库名字
        'USER': 'root',          #账号
        'PASSWORD': '19920202qwer',    #密码
        'HOST': '120.77.223.13',     #IP
        'PORT': '3306',          #端口
        #这里引擎用innodb（默认myisam）
        #因为后面第三方登录时，要求引擎为INNODB
        # 'OPTIONS':{'init_command': 'SET storage_engine=INNODB'}, #这样设置会报错，改为
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# debug-toolbar
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
INTERNAL_IPS = ('127.0.0.1',)





#有效期限
JWT_AUTH = {
    # 允许刷新
    'JWT_ALLOW_REFRESH': True,
    # 允许续期
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=24),

    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),    #也可以设置seconds=20
    'JWT_AUTH_HEADER_PREFIX': 'JWT',                       #JWT跟前端保持一致，比如“token”这里设置成JWT
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utils.users.jwt_response_payload_handler',
    # 自定义用户的secret_key
    # 'JWT_GET_USER_SECRET_KEY': 'utils.users.jwt_get_user_secret',

}

REST_FRAMEWORK = {
    # #分页
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # #每页显示的个数
    # 'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'system.permissions.IsOwnerOrReadOnly',
        # 设置要求登陆,原先登陆的会无效
        'rest_framework.permissions.IsAuthenticated',
        # 'system.permissions.IsOwnerOrReadOnly',

    ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework_csv.renderers.CSVRenderer',
    # ),
    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema',
}

AUTH_USER_MODEL = 'system.UserProfile'

# LOGGING settings
LOG_DIR = BASE_DIR + "/log"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s FuncName:%(funcName)s LINE:%(lineno)d [%(levelname)s]- %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'maxBytes': 1024*1024*50,   # 50 MB
            'backupCount': 2,
            'formatter': 'standard',
        },
        'default_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'maxBytes': 1024*1024*50,  # 50 MB
            'backupCount': 2,
            'formatter': 'standard',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'common.log'),
            'maxBytes': 1024*1024*50,  # 50 MB
            'backupCount': 2,
            'formatter': 'standard',
        },
        'restful_api': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'api.log'),
            'maxBytes': 1024*1024*50,  # 50 MB
            'backupCount': 2,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'default_debug'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'common': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True
        },
        'api': {
            'handlers': ['restful_api'],
            'level': 'INFO',
            'propagate': True
        },
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True


CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:9001',
    'http://0.0.0.0:9001',
    'http://0.0.0.0:8000',
    'http://0.0.0.0:3000',
    'http://0.0.0.0:8080',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = default_headers + (
    'Access-Control-Allow-Headers',
    'Access-Control-Allow-Origin',
    'token',
    'x-token',
)


# redis配置
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100},
#             "PASSWORD": "xxx",
#         }
#     }
# }

djcelery.setup_loader()
# 在文件中添加下面的两行配置
#数据库调度
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_RESULT_BACKEND = 'redis://:19920202qwer@localhost:6379/0'
# result_backend = 'redis://:19920202qwer@localhost:6379/0'
# BROKER_URL= 'amqp://ccc:123456qwer@120.24.167.214:5672'
# CELERY_ACCEPT_CONTENT = ['application/json',]
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Shanghai'