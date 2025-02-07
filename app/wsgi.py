"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from os import path, getenv
from dotenv import load_dotenv
from app.settings.base import local_env_file


if path.isfile(local_env_file):
    load_dotenv(local_env_file)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'app.settings.{getenv('MODE')}')

application = get_wsgi_application()
