from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.decorators import user_passes_test

from django.urls import reverse

from django.conf import settings
from django.views.decorators.cache import never_cache
from django.core.exceptions import ObjectDoesNotExist

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

import colorama, threading
from uptimebot import models
from uptimecheckcore.components.helpers.configurations import is_secretkey_insecure
from uptimebot.handler import check_domains, check_domain

@never_cache
@user_passes_test(operator_privilege_check)
def index(request):

    return render( request, "panel/index.html",
                              {
                                  'title' : 'Uptime Checker Dashboard',
                                  'is_secretkey_insecure' : is_secretkey_insecure,
                              })

@never_cache
@user_passes_test(operator_privilege_check)
def settings(request):
    return render( request, "panel/settings.html",
                              {
                                  'title': 'Settings',

                                  'is_secretkey_insecure' : is_secretkey_insecure,
                              })


@never_cache
@user_passes_test(operator_privilege_check)
def users(request):
    return render( request, "panel/users.html",
                              {
                                  'title': 'Users',

                                  'is_secretkey_insecure' : is_secretkey_insecure,
                              })

@api_view(['GET', 'POST',])
@authentication_classes(( SessionAuthentication, ))
@permission_classes((IsOperatorAuthenticated,))
def api_uptime_list(request):
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
                'status_display' : u.get_status_display(),
                'end_time' : f'{u.end_time}'
            } )
        timestamp = None
        if s.ssl_expire_time:
            timestamp = s.ssl_expire_time.timestamp()

        results.append({
            'id' : f'{s.id}',
            'title' : s.title,
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
    if settings.DEBUG:
        print(f"{colorama.Fore.RED}request user is:{colorama.Style.RESET_ALL} {request.user.username}")
        print(f">> request.data: {request.data}")

    if "mode" in request.data and request.data["mode"]:
        if request.data["mode"] == "all":
            check_domains()

            message = "Refresh all triggered"

            return JsonResponse({
                'message' : message,
                'status' : 'okay'
            })
        elif request.data["mode"] == "single" and "host_id" in request.data:
            host_id = request.data["host_id"]
            try:
                the_website = models.TargetWebsite.objects.get(id=host_id)
            except ObjectDoesNotExist:
                return JsonResponse({
                    'error': "Website does not exist",
                    'status': 'error'
                })

            t = threading.Thread(target=check_domain,
                                 args=[the_website, ],
                                 kwargs={})
            t.start()

            message = "Refresh for single website triggered"
            return JsonResponse({
                'message' : message,
                'status' : 'okay'
            })



    return JsonResponse({
        'error': "Invalid trigger request",
        'status': 'error'
    })
