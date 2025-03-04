from os import path, getenv
from dotenv import load_dotenv
from app.settings.base import local_env_file


if path.isfile(local_env_file):
    load_dotenv(local_env_file)


"""
Do read:

    1. https://docs.djangoproject.com/en/3.1/ref/settings/#sessions
    2. https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
"""
SESSION_COOKIE_AGE = int(getenv('SESSION_COOKIE_AGE', default=1209600))  # Default - 2 weeks in seconds
SESSION_COOKIE_HTTPONLY = getenv('SESSION_COOKIE_HTTPONLY', default=True)
SESSION_COOKIE_NAME = getenv('SESSION_COOKIE_NAME', default='sessionid')
SESSION_COOKIE_SAMESITE = getenv('SESSION_COOKIE_SAMESITE', default='strict')
SESSION_COOKIE_SECURE = getenv('SESSION_COOKIE_SECURE', default=False)


CSRF_USE_SESSIONS = getenv('CSRF_USE_SESSIONS', default=True)