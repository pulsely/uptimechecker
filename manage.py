#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import colorama, threading, time
from uptimecheckcore.components.helpers import first_run
from django.core.management import call_command

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

def migrate_thread():
    print(f"{colorama.Fore.GREEN}Creating SQLite database in {colorama.Fore.RED}4{colorama.Fore.GREEN} seconds{colorama.Style.RESET_ALL}")
    time.sleep(4)
    print(f"{colorama.Fore.GREEN}Creating SQLite database in {colorama.Fore.RED}3{colorama.Fore.GREEN} seconds{colorama.Style.RESET_ALL}")
    time.sleep(3)
    print(f"{colorama.Fore.GREEN}Creating SQLite database in {colorama.Fore.RED}2{colorama.Fore.GREEN} seconds{colorama.Style.RESET_ALL}")
    time.sleep(2)
    print(f"{colorama.Fore.GREEN}Creating SQLite database in {colorama.Fore.RED}1{colorama.Fore.GREEN} seconds{colorama.Style.RESET_ALL}")
    time.sleep(1)
    print(f"{colorama.Fore.GREEN}Creating...{colorama.Style.RESET_ALL}")

    call_command('migrate', verbosity=0, interactive=True)
    print(
        f"{colorama.Fore.RED}Done! {colorama.Fore.GREEN}Database should be ready to go!{colorama.Style.RESET_ALL}")

    print(
        f"If the database file is not created, just run: {colorama.Fore.RED}python manage.py migrate{colorama.Style.RESET_ALL}")


if __name__ == '__main__':
    # Check if there is a .env file? If not create the settings
    if os.path.exists( ".env"):

        main()
    else:
        print(f"{colorama.Fore.RED}Your system has not initialized.{colorama.Style.RESET_ALL}")

        # Create a .env file
        print(f"{colorama.Fore.GREEN}Create a .env file with default settings{colorama.Style.RESET_ALL}")
        first_run.create_default_file()

        # Schedule migrate thread in 3 seconds
        thread_ = threading.Thread(target=migrate_thread,
                                             args=[],
                                             kwargs={})
        # sessiontag_thread.setDaemon(True)
        thread_.start()

        # Run migrate
        main()

