from django.conf import settings

def is_secretkey_insecure():
    if settings.SECRET_KEY and settings.SECRET_KEY.startswith("default-insecure-change-this"):
        return True
    else:
        return False
