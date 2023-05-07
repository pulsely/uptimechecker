import os

import colorama
import getpass
from django.core.management.utils import get_random_secret_key
from django.contrib.auth import get_user_model

def create_default_file():
    '''
    # The file should be in the following format:
    PYTHONDONTWRITEBYTECODE=true
    DEBUG=true
    SECRET_KEY=""
    ALLOWED_HOSTS="*"
    DEFAULT_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
    DEFAULT_PERIODIC_MINUTES=7
    '''

    SECRET_KEY = get_random_secret_key()

    f = open(".env", "a")

    f.write("PYTHONDONTWRITEBYTECODE=true")
    f.write("\n")
    f.write("DEBUG=true")
    f.write("\n")

    f.write(f'SECRET_KEY="{SECRET_KEY}"')
    f.write("\n")
    f.write('ALLOWED_HOSTS="*"')
    f.write("\n")
    f.write('DEFAULT_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"')
    f.write("\n")
    f.write("DEFAULT_PERIODIC_MINUTES=15")
    f.close()

def create_first_user():
    User = get_user_model()

    print(f"{colorama.Fore.RED}You do not have any user in the system yet.{colorama.Style.RESET_ALL}")
    print("Now, set the username and password of your superuser:")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    print(f"Creating with your username {colorama.Fore.GREEN}{username}{colorama.Style.RESET_ALL} and {colorama.Fore.GREEN}********{colorama.Style.RESET_ALL}")

    the_user = User.objects.create_user( username, '', password)
    the_user.is_staff = True
    the_user.is_superuser = True
    the_user.save()
    print("User created. You can now sign in.")

