#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import colorama
from uptimecheckcore.components.helpers import first_run

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uptimechecker.settings')
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
    # Check if there is a uptimechecker/settings_customized file?
    first_run.check_and_create_settings_customized()

    # Check if there is a .env file? If not create the .env settings
    first_run.check_and_create_env()

    main()
