"""
Django settings for service project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Site (Custom)
SITE_PROTOCOL = os.getenv("SITE_PROTOCOL", "http")
SITE_DOMAIN = os.getenv("SITE_DOMAIN", "localhost")
SITE_PORT = int(os.getenv("SITE_PORT", "8000"))
SITE_BASE_URL = f"{SITE_PROTOCOL}://{SITE_DOMAIN}:{SITE_PORT}"
SITE_API_URL = f"{SITE_BASE_URL}/api"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "not-a-secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv("DEBUG", "1")))

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "aimmo",
    "game",
    "pipeline",
    "portal",
    "captcha",
    "common",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "rest_framework",
    "import_export",
    "django_js_reverse",
    "django_otp",
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "sekizai",  # for javascript and css management
    "treebeard",
    "two_factor",
    "preventconcurrentlogins",
    # "codeforlife",
    "corsheaders",
]

MIDDLEWARE = [
    "deploy.middleware.admin_access.AdminAccessMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "deploy.middleware.security.CustomSecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "deploy.middleware.session_timeout.SessionTimeoutMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "deploy.middleware.exceptionlogging.ExceptionLoggingMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware",
    "csp.middleware.CSPMiddleware",
    # "deploy.middleware.screentime_warning.ScreentimeWarningMiddleware",
]

ROOT_URLCONF = "service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "common.context_processors.module_name",
                "common.context_processors.cookie_management_enabled",
                # TODO: use when integrating dotmailer
                # "portal.context_processors.process_newsletter_form",
            ]
        },
    }
]

WSGI_APPLICATION = "service.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Auth
# https://docs.djangoproject.com/en/3.2/topics/auth/default/

LOGIN_URL = f"{SITE_API_URL}/login/session-expired/"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-gb"

LANGUAGES = [("en-gb", "English")]

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "portal/static"]
STATICFILES_FINDERS = [
    "pipeline.finders.PipelineFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
# STATICFILES_STORAGE = "pipeline.storage.PipelineStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Sessions
# https://docs.djangoproject.com/en/3.2/topics/http/sessions/

SESSION_COOKIE_AGE = 60 * 60
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"

# CSRF
# https://docs.djangoproject.com/en/3.2/ref/csrf/

# TODO: determine if the below is needed.
# CSRF_COOKIE_SAMESITE = "None"
# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True

# CORS
# https://pypi.org/project/django-cors-headers/

CORS_ALLOW_ALL_ORIGINS = DEBUG
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = []

# Logging
# https://docs.djangoproject.com/en/3.2/topics/logging/

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(asctime)s][%(name)s][%(levelname)s] %(message)s",
            "style": "%",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    # TODO: check if this is needed
    # "loggers": {
    #     "two_factor": {
    #         "handlers": ["console"],
    #         "level": "INFO",
    #     },
    # },
    "root": {
        "level": os.getenv("LOG_LEVEL", "INFO"),
        "handlers": ["console"],
    },
}


# Custom
MEDIA_ROOT = os.path.join(STATIC_ROOT, "email_media/")
LOGIN_REDIRECT_URL = "/teach/dashboard/"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"


CODEFORLIFE_WEBSITE = "www.codeforlife.education"
CLOUD_STORAGE_PREFIX = "https://storage.googleapis.com/codeforlife-assets/"
# TODO: assess if still need and trim fat if not.
# RAPID_ROUTER_EARLY_ACCESS_FUNCTION_NAME = "portal.beta.has_beta_access"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
RECAPTCHA_DOMAIN = "www.recaptcha.net"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    # "portal.backends.StudentLoginBackend",
]
PASSWORD_RESET_TIMEOUT_DAYS = 1

PIPELINE_ENABLED = False

# This is used in common to enable/disable the OneTrust cookie management script
COOKIE_MANAGEMENT_ENABLED = False

AUTOCONFIG_INDEX_VIEW = "home"
SITE_ID = 1

PIPELINE = {}

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

MODULE_NAME = os.getenv("MODULE_NAME")

# Domain
def domain():
    """Returns the full domain depending on whether it's local, dev, staging or prod."""
    domain_name = "https://www.codeforlife.education"

    if MODULE_NAME == "local":
        domain_name = "localhost:8000"
    elif MODULE_NAME == "staging":
        domain_name = f"https://staging-dot-decent-digit-629.appspot.com"
    elif MODULE_NAME == "dev":
        domain_name = f"https://development-portal-dot-decent-digit-629.appspot.com"

    return domain_name


CSP_DEFAULT_SRC = ("self",)
CSP_CONNECT_SRC = (
    "'self'",
    "https://api.pwnedpasswords.com",
    "https://*.onetrust.com/",
    "https://euc-widget.freshworks.com/",
    "https://codeforlife.freshdesk.com/",
    "https://api.iconify.design/",
    "https://api.simplesvg.com/",
    "https://api.unisvg.com/",
    "https://www.google-analytics.com/",
    "https://region1.google-analytics.com/g/",
    "https://pyodide-cdn2.iodide.io/v0.15.0/full/",
    "https://crowdin.com/",
    "https://o2.mouseflow.com/",
    "https://stats.g.doubleclick.net/",
    f"wss://{MODULE_NAME}-aimmo.codeforlife.education/",
    f"https://{MODULE_NAME}-aimmo.codeforlife.education/",
)
CSP_FONT_SRC = (
    "'self'",
    "https://fonts.gstatic.com/",
    "https://fonts.googleapis.com/",
    "https://use.typekit.net/",
)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "https://cdn.crowdin.com/",
    "https://*.onetrust.com/",
    "https://code.jquery.com/",
    "https://euc-widget.freshworks.com/",
    "https://cdn-ukwest.onetrust.com/",
    "https://code.iconify.design/2/2.0.3/iconify.min.js",
    "https://www.googletagmanager.com/",
    "https://www.google-analytics.com/analytics.js",
    "https://cdn.mouseflow.com/",
    "https://www.recaptcha.net/",
    "https://www.google.com/recaptcha/",
    "https://www.gstatic.com/recaptcha/",
    "https://use.typekit.net/mrl4ieu.js",
    "https://pyodide-cdn2.iodide.io/v0.15.0/full/",
    f"{domain()}/static/portal/",
    f"{domain()}/static/common/",
    "https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js",
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    "https://euc-widget.freshworks.com/",
    "https://cdn-ukwest.onetrust.com/",
    "https://fonts.googleapis.com/",
    "https://code.jquery.com/ui/1.13.1/themes/base/jquery-ui.css",
    "https://cdn.crowdin.com/",
    f"{domain()}/static/portal/",
)
CSP_FRAME_SRC = (
    "https://storage.googleapis.com/",
    "https://www.youtube-nocookie.com/",
    "https://www.recaptcha.net/",
    "https://www.google.com/recaptcha/",
    "https://crowdin.com/",
    f"{domain()}/static/common/img/",
    f"{domain()}/static/game/image/",
)
CSP_IMG_SRC = (
    "https://storage.googleapis.com/codeforlife-assets/images/",
    "https://cdn-ukwest.onetrust.com/",
    "https://p.typekit.net/",
    "https://cdn.crowdin.com/",
    "https://crowdin-static.downloads.crowdin.com/",
    "https://www.google-analytics.com/",
    "data:",
    f"{domain()}/static/portal/img/",
    f"{domain()}/static/portal/static/portal/img/",
    f"{domain()}/static/portal/img/",
    f"{domain()}/favicon.ico",
    f"{domain()}/img/",
    f"{domain()}/account/two_factor/qrcode/",
    f"{domain()}/static/",
    f"{domain()}/static/game/image/",
    f"{domain()}/static/game/raphael_image/",
    f"{domain()}/static/game/js/blockly/media/",
    f"{domain()}/static/icons/",
)
CSP_OBJECT_SRC = (
    f"{domain()}/static/common/img/",
    f"{domain()}/static/game/image/",
)
CSP_MEDIA_SRC = (
    f"{domain()}/static/react/",
    f"{domain()}/static/game/sound/",
    f"{domain()}/static/game/js/blockly/media/",
    f"{domain()}/static/portal/video/",
)
CSP_MANIFEST_SRC = (f"{domain()}/static/manifest.json",)
