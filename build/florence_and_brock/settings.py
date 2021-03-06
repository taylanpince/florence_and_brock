import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Taylan Pince', 'taylanpince@gmail.com'),
    ('Sam Bull', 'osirius@gmail.com'),
    ('Dael Stewart', 'dstew19@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Canada/Eastern'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'

SECRET_KEY = 'b_n_3$(b+5_h1c@cu!dp2xa92bvshzjs*z1ytcrdkmifo=^diq'

AUTHENTICATION_BACKENDS = (
    'residents.backends.ResidentUserBackend',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'florence_and_brock.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.realpath(os.path.dirname(__file__)), 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',

    'django_evolution',
    'django_extensions',
    'sorl.thumbnail',

    'decisions',
    'houses',
    'residents',
    'pagination',
    'quicklinks',
    'documents',
    'news',
)

try:
    from settings_local import *
except ImportError:
    pass
