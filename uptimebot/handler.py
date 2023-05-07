import requests
import colorama
from django.utils import timezone

from django.conf import settings
import threading, pytz, datetime
from random import randint
from time import sleep
import colorama
from . import models
import secrets
from django.conf import settings

# https://stackoverflow.com/questions/16903528/how-to-get-response-ssl-certificate-from-requests-in-python

HTTPResponse = requests.packages.urllib3.response.HTTPResponse
orig_HTTPResponse__init__ = HTTPResponse.__init__
def new_HTTPResponse__init__(self, *args, **kwargs):
    orig_HTTPResponse__init__(self, *args, **kwargs)
    try:
        self.peercert = self._connection.sock.getpeercert()
    except AttributeError:
        pass
HTTPResponse.__init__ = new_HTTPResponse__init__

HTTPAdapter = requests.adapters.HTTPAdapter
orig_HTTPAdapter_build_response = HTTPAdapter.build_response
def new_HTTPAdapter_build_response(self, request, resp):
    response = orig_HTTPAdapter_build_response(self, request, resp)
    try:
        response.peercert = resp.peercert
    except AttributeError:
        pass
    return response
HTTPAdapter.build_response = new_HTTPAdapter_build_response

def check_domain( target_website ):
    url = target_website.url
    url = url.strip()

    if target_website.flag_cdn_random_key:
        random = secrets.token_hex()
        url = f'{url}?r={random}'

    #if settings.DEBUG:
    #    print(f'{colorama.Fore.RED}Check url>{colorama.Style.RESET_ALL} {url}')

    u = models.UptimeCheck()
    u.url = url
    u.status = "checking"
    u.target_website = target_website
    u.start_time = timezone.now()
    u.save()

    try:
        if settings.DEFAULT_ADD_RANDOMNESS:
            sleep(randint(1, 30))        # add random
        r = requests.get( url, headers={ 'User-Agent' : settings.DEFAULT_USER_AGENT }, timeout=15 )
        if r.status_code == 200:
            u.status = 'normal'
            u.status_code = r.status_code
            u.end_time = timezone.now()

            if target_website.must_contain_keyword and len(target_website.must_contain_keyword) > 0:
                if r.text.find( target_website.must_contain_keyword ) < 0:
                    u.status = "missing_keyword"
                    if target_website.flag_notify_downtime:
                        post_notification( 'Missing keyword: ', f'{target_website.url} has status {u.status}' )

            if target_website.flag_check_ssl_expire_time:
                # if settings.DEBUG:
                #     print(f"{colorama.Fore.RED}r.peercert:{colorama.Style.RESET_ALL} {r.peercert}")
                ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
                expire_time_naive = datetime.datetime.strptime( r.peercert['notAfter'], ssl_date_fmt)
                expire_time_datetime = pytz.timezone('UTC').localize(expire_time_naive)

                if target_website.ssl_expire_time != expire_time_datetime:
                    target_website.ssl_expire_time = expire_time_datetime
                    target_website.save()

            u.save()

            if settings.DEBUG:
                print( f"{colorama.Fore.GREEN}{url} is up{colorama.Style.RESET_ALL}")
        else:
            u.status = 'error'
            u.status_code = r.status_code
            u.end_time = timezone.now()
            u.save()

            if settings.DEBUG:
                print( f"{colorama.Fore.RED}{url} throw error code:{colorama.Style.RESET_ALL} {r.status_code}")

            if target_website.flag_notify_downtime:
                post_notification( 'Server down', f'{target_website.url} has status {u.status}' )
    except Exception as e:
        u.status = 'exception'
        #u.status_code = r.status_code
        u.payload = {
            'exception' : f'{e}'
        }
        u.end_time = timezone.now()
        u.error_description = f'{e}'
        #u.exception = f'{e}'
        u.save()

        if settings.DEBUG:
            print(f"{colorama.Fore.RED}{url} throw exception:{colorama.Style.RESET_ALL} {e}")
        post_notification( 'Server down', f'{target_website.url} has status {u.status}' )

def check_domains():
    if settings.DEBUG:
        print(f"{colorama.Fore.GREEN}check_domains:{colorama.Style.RESET_ALL} - %s" % timezone.now())
    #urls = ['https://fleur.hk/', 'https://www.pulsely.com/', 'https://consultingerp.pulsely.com/']

    for w in models.TargetWebsite.objects.all():
        if settings.DEBUG:
            print(f"{colorama.Fore.RED}check_domains{colorama.Style.RESET_ALL} URL: {colorama.Fore.GREEN}%s{colorama.Style.RESET_ALL}" % w.url)
        t = threading.Thread(target=check_domain,
                                           args=[w, ],
                                           kwargs={})
        t.start()

def post_notification( title, body ):
    pass

def remove_expired_uptimes():
    previous_cutoff = timezone.now() - datetime.timedelta(days=3)

    matching_checks = models.UptimeCheck.objects.filter( status="normal", start_time__lte=datetime.datetime( previous_cutoff.year, previous_cutoff.month, previous_cutoff.day, 0, 0, 0, 0 ) )
    if settings.DEBUG:
        print(f"{colorama.Fore.RED}remove_expired_uptimes:{colorama.Style.RESET_ALL} Delete %d matching time" % len(matching_checks))
    matching_checks.delete()


