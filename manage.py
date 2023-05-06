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
    # Check if there is a .env file? If not create the settings
    if os.path.exists( ".env"):

        main()
    else:
        print(f"{colorama.Fore.RED}Your system has not initialized.{colorama.Style.RESET_ALL}")
        first_run.create_default_file()