import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Chave secreta do Django
import os
from decouple import config
SECRET_KEY = config('DJANGO_SECRET_KEY', default='chave-fallback-insegura')




# Debug
DEBUG = True  # Defina como False em produção

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'clinica-django-056n.onrender.com',
]


# Aplicativos instalados
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'usuarios',
    'pacientes',
    'profissionais',
    'procedimentos',
    'agendamentos',
    'cadastros',
    'salas',
    'home',
    "widget_tweaks",
]

# Middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Configuração das URLs
ROOT_URLCONF = "meu_projeto.urls"

# Configurações dos templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Configuração WSGI
WSGI_APPLICATION = "meu_projeto.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Diretório onde o collectstatic irá armazenar os arquivos (usado em produção)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Diretórios onde o Django procurará por arquivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# Configuração do tipo de chave primária padrão
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # Lê o email do .env
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Lê a senha do .env
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

PASSWORD_RESET_TIMEOUT = 60 * 60 * 24  # 1 dia

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'usuarios.backends.EmailBackend',
]

# URL de login padrão
LOGIN_URL = 'usuarios:login'

# URL de redirecionamento após o login
LOGIN_REDIRECT_URL = 'agendamentos:listar_agendamentos'

# URL de redirecionamento após o logout
LOGOUT_REDIRECT_URL = 'usuarios:login'