#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from os import path, getenv
from dotenv import load_dotenv
from app.settings.base import local_env_file


if path.isfile(local_env_file):
    load_dotenv(local_env_file)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'app.settings.{getenv('MOOD')}')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
