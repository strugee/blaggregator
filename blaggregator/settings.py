import os
import sys
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# True: heroku config:set DJANGO_DEBUG=True
# False: heroku config:unset DJANGO_DEBUG
DEBUG = 'DJANGO_DEBUG' in os.environ

if os.environ.get('PROD', None):
    print "** DETECTED PRODUCTION ENVIRONMENT"

    # S3
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'blaggregator'

    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

elif os.environ.get('STAGING', None):
    print "** DETECTED STAGING ENVIRONMENT"

    # S3
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'blaggregator-staging'

    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

else:
    print "** DETECTED LOCAL ENVIRONMENT"
    STATIC_URL = '/static/'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Sasha Laundy', 'sasha.laundy@gmail.com'),
    ('Puneeth Chaganti', 'punchagan@muse-amuse.in'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blaggregator_dev',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'sasha',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'NAME': 'blaggregator_test',
            'ENGINE': 'django.db.backends.sqlite3',
        }
    }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'localhost',
    'blaggregator.herokuapp.com',
    'blaggregator-staging.herokuapp.com',
    'www.blaggregator.us',
    'blaggregator.recurse.com'
]

# Use HTTP_X_FORWARDED_HOST header to construct absolute URIs
USE_X_FORWARDED_HOST = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static-collected')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('BLAGGREGATOR_SECRET_KEY',
                            '%dut3)!1f(nm0x8bm@tuj!*!2oe=+3+bsw2lf0)%(4l8d2^z8s')

MIDDLEWARE_CLASSES = (
    'home.middleware.RecurseSubdomainMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'blaggregator.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'blaggregator.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'home.context_processors.primary_blog',
            ]
        }
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'django.contrib.admin',
    'storages',
    'django.contrib.humanize',
    'social.apps.django_app.default',
)

AUTHENTICATION_BACKENDS = (
    'home.oauth.HackerSchoolOAuth2',
    'home.token_auth.TokenAuthBackend',
)

LOGIN_URL = '/login/'
SOCIAL_AUTH_HACKERSCHOOL_KEY = os.environ.get('SOCIAL_AUTH_HS_KEY', None)
SOCIAL_AUTH_HACKERSCHOOL_SECRET = os.environ.get('SOCIAL_AUTH_HS_SECRET', None)
SOCIAL_AUTH_HACKERSCHOOL_LOGIN_URL = '/login'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/new/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'

if os.environ.get('PROD', None):
    SOCIAL_AUTH_HACKERSCHOOL_REDIRECT_URL = 'http://www.blaggregator.us/complete/hackerschool'
elif os.environ.get('STAGING', None):
    SOCIAL_AUTH_HACKERSCHOOL_REDIRECT_URL = 'http://blaggregator-staging.herokuapp.com/complete/hackerschool'
else:
    SOCIAL_AUTH_HACKERSCHOOL_REDIRECT_URL = 'http://localhost:8000/complete/hackerschool'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'home.oauth.find_legacy_user',
    'social.pipeline.user.get_username',
    'home.oauth.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'home.oauth.create_or_update_hacker'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler"
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ["console"],
            'level': 'ERROR',
            'propagate': True,
        },
        "blaggregator": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        }
    }
}

# This bit uses the module dj_database_url to manage databases based on the
# url of the database, as configured in environmental variables (which are
# in turn managed by the Heroku Postgres add-on)
if os.environ.get('PROD', '') or os.environ.get('STAGING', ''):

    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Feed configuration

# Maximum number of entries to have in the feed.  To balance between sending a
# huge feed and forcing users to update feed super-frequently, a good value for
# this would be around twice the average number of posts in a week.
MAX_FEED_ENTRIES = 100

# Max number of posts per blog to announce on Zulip per crawl
MAX_POST_ANNOUNCE = 2
