import os
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent.parent


def load_env_file(env_path: Path) -> dict[str, str]:
    env_values: dict[str, str] = {}
    if not env_path.exists():
        return env_values

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env_values[key.strip()] = value.strip()
    return env_values


def build_database_config(base_dir: Path) -> dict[str, dict[str, object]]:
    env_values = load_env_file(base_dir / ".env")
    jdbc_url = env_values.get("URL", "")
    username = env_values.get("user", "")
    password = env_values.get("Password", "")
    explicit_port = env_values.get("Port", "")

    if jdbc_url.startswith("jdbc:postgresql://") and username and password:
        parsed = urlparse(jdbc_url.replace("jdbc:", "", 1))
        database_name = parsed.path.lstrip("/") or "postgres"
        port = explicit_port or parsed.port or "5432"
        return {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": database_name,
                "USER": username,
                "PASSWORD": password,
                "HOST": parsed.hostname or "localhost",
                "PORT": str(port),
            }
        }

    return {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": base_dir / "db.sqlite3",
        }
    }


SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-dbzl44s$jf4!6+_67ab#=(6ly#zb#p_m!il0k))c1kj=ucjw+g",
)
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "academics",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "university_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "university_api.wsgi.application"

DATABASES = build_database_config(BASE_DIR)

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Kiev"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
