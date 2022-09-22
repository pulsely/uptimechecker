from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.decorators import user_passes_test

from django.urls import reverse

from django.conf import settings
from django.views.decorators.cache import never_cache

from uptimecheckcore.components.credentials.privileges import operator_privilege_check, IsOperatorAuthenticated
#from rest_framework_simplejwt.authentication import JWTAuthentication

#from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    renderer_classes,
    parser_classes,
    authentication_classes,
    throttle_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication

import colorama
from uptimebot import models

@never_cache
@user_passes_test(operator_privilege_check)
def index(request):

    return render( request, "panel/index.html",
                              {
                                  'SAAS_TEMPLATE_STYLE' : 'navbar-white-header',
                                  'flag_nav_spacer': True
                              })


@api_view(['GET', 'POST',])
@authentication_classes(( SessionAuthentication, ))
@permission_classes((IsOperatorAuthenticated,))
def api_uptime_list(request):
    if settings.DEBUG:
        print(f"{colorama.Fore.RED}request user is:{colorama.Style.RESET_ALL} {request.user.username}")
    results = []

    for s in models.TargetWebsite.objects.order_by('url',):
        try:
            previous_exception_ = models.UptimeCheck.objects.filter(target_website=s,
                                                                   status__in=['error', 'exception',
                                                                               'missing_keyword']).order_by(
                '-start_time', )[0]

            previous_exception = {
                'time' : previous_exception_.end_time.timestamp(),
                'status' : previous_exception_.status
            }
        except:
            previous_exception = None

        # models.UptimeCheck.objects.
        uptimes = []
        for u in models.UptimeCheck.objects.filter(target_website=s).order_by( '-start_time', )[:5]:
            uptimes.append( {
                'status' : u.status,
                'status_code' : u.status_code,
                'end_time' : f'{u.end_time}'
            } )
        timestamp = None
        if s.ssl_expire_time:
            timestamp = s.ssl_expire_time.timestamp()

        results.append({
            'id' : f'{s.id}',
            'target_website_url': f'{s.url}',
            'ssl_expire_time' : timestamp,
            'uptimes': uptimes,
            'previous_exception' : previous_exception,

        })

    return JsonResponse({
        'results' : results,
        'status' : 'okay'
    })

@api_view(['GET', 'POST',])
#@authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes(( SessionAuthentication, ))
@permission_classes((IsOperatorAuthenticated,))
def api_trigger_refresh(request):
    if request.user.is_staff:
        if settings.DEBUG:
            print(f"{colorama.Fore.RED}request user is:{colorama.Style.RESET_ALL} {request.user.username}")
        results = []

        for s in models.TargetWebsite.objects.order_by('url',):
            try:
                previous_exception_ = models.UptimeCheck.objects.filter(target_website=s,
                                                                       status__in=['error', 'exception',
                                                                                   'missing_keyword']).order_by(
                    '-start_time', )[0]

                previous_exception = {
                    'time' : previous_exception_.end_time.timestamp(),
                    'status' : previous_exception_.status
                }
            except:
                previous_exception = None

            # models.UptimeCheck.objects.
            uptimes = []
            for u in models.UptimeCheck.objects.filter(target_website=s).order_by( '-start_time', )[:5]:
                uptimes.append( {
                    'status' : u.status,
                    'status_code' : u.status_code,
                    'end_time' : f'{u.end_time}'
                } )
            timestamp = None
            if s.ssl_expire_time:
                timestamp = s.ssl_expire_time.timestamp()

            results.append({
                'id' : f'{s.id}',
                'target_website_url': f'{s.url}',
                'ssl_expire_time' : timestamp,
                'uptimes': uptimes,
                'previous_exception' : previous_exception,

            })

        return JsonResponse({
            'results' : results,
            'status' : 'okay'
        })
    else:
        return JsonResponse({
            'status' : 'error',
            'error' : 'User does not have privilege'
        })