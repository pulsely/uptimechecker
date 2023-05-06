import os
from django.core.management.utils import get_random_secret_key

def create_default_file():
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
    f.write("DEFAULT_PERIODIC_MINUTES=7")
    f.close()
    '''
PYTHONDONTWRITEBYTECODE=true
DEBUG=true
SECRET_KEY="n$0gdvf=s&oqa4ap99%@tyu7m$dey4=(3#e^h$_!2qd%bk2m$)"
ALLOWED_HOSTS="*"
DEFAULT_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
DEFAULT_PERIODIC_MINUTES=7
    '''