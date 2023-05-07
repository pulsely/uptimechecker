from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout

from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.core.exceptions import ObjectDoesNotExist
from uptimecheckcore.components.helpers.first_run import first_run_has_no_users, is_docker
from uptimecheckcore.components.credentials.privileges import operator_privilege_check, staff_privilege_check,\
    IsOperatorAuthenticated, IsStaffAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

# from rest_framework.permissions import IsAuthenticated
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
from uptimecheckcore.components.helpers import Slack
from uptimebot.handler import check_domains, check_domain
from . import forms
from django.contrib.auth import login
from django.core.mail import send_mail

User = get_user_model()

@never_cache
@user_passes_test(operator_privilege_check)
def index(request):
    return render(request, "panel/index.html",
                  {
                      'title': 'Uptime Checker Dashboard',
                      'is_secretkey_insecure': is_secretkey_insecure,
                      'flag_show_create_website_button' : True,
                  })


@never_cache
@user_passes_test(staff_privilege_check)
def configurations(request):

    return render(request, "panel/configurations.html",
                  {
                      'title': 'Configurations',


                      'DATABASES': settings.DATABASES,

                      'DEBUG_': settings.DEBUG,

                      'ALLOWED_HOSTS_': settings.ALLOWED_HOSTS,

                      'REDIS_URL_': settings.REDIS_URL,

                      'CELERY_TIMEZONE_': settings.CELERY_TIMEZONE,

                      'CELERY_TASK_TRACK_STARTED_': settings.CELERY_TASK_TRACK_STARTED,
                      'CELERY_TASK_TIME_LIMIT_': settings.CELERY_TASK_TIME_LIMIT,

                      'DEFAULT_PERIODIC_MINUTES_': settings.DEFAULT_PERIODIC_MINUTES,
                      'DEFAULT_ADD_RANDOMNESS' : settings.DEFAULT_ADD_RANDOMNESS,
                      'DEFAULT_PERIODIC_MINUTES' : settings.DEFAULT_PERIODIC_MINUTES,

                      'EMAIL_BACKEND' : settings.EMAIL_BACKEND,
                      'AWS_SES_REGION_NAME' : settings.AWS_SES_REGION_NAME,
                      'AWS_SES_REGION_ENDPOINT' : settings.AWS_SES_REGION_ENDPOINT,
                      'SERVER_EMAIL' : settings.SERVER_EMAIL,

                      'DEFAULT_USER_AGENT' : settings.DEFAULT_USER_AGENT,

                      'SLACK_TOKEN' : settings.SLACK_TOKEN,
                      'SLACK_ROOM' : settings.SLACK_ROOM,

                  })


@never_cache
@user_passes_test(staff_privilege_check)
def users(request):
    return render(request, "panel/users/index.html",
                  {
                      'title': 'Users',

                      'is_secretkey_insecure': is_secretkey_insecure,
                  })

@never_cache
@user_passes_test(staff_privilege_check)
def users_create(request):
    return render(request, "panel/users/edit.html",
                  {
                      'title': 'Create new user',

                      'is_secretkey_insecure': is_secretkey_insecure,

                      'operation' : "create",
                  })

@never_cache
@user_passes_test(staff_privilege_check)
def users_edit(request, user_id):

    the_user = get_object_or_404( User, id=user_id )

    return render(request, "panel/users/edit.html",
                  {
                      'title': 'User edit',
                      'is_secretkey_insecure': is_secretkey_insecure,
                      'operation': "edit",
                      'the_user' : the_user,
                  })

@never_cache
@user_passes_test(staff_privilege_check)
def users_reset_password(request, user_id):
    the_user = get_object_or_404( User, id=user_id )

    return render(request, "panel/users/reset_password.html",
                  {
                      'title': f'Reset password for {the_user.username}',
                      'is_secretkey_insecure': is_secretkey_insecure,
                      'operation': "edit",
                      'the_user' : the_user,
                  })

@never_cache
@user_passes_test(operator_privilege_check)
def change_password(request):
    the_user = request.user

    return render(request, "panel/users/change_password.html",
                  {
                      'title': f'Change password for {the_user.username}',
                      'is_secretkey_insecure': is_secretkey_insecure,
                      'operation': "edit",
                      'the_user' : the_user,
                  })


@never_cache
@user_passes_test(staff_privilege_check)
def websites_create(request):

    return render(request, "panel/websites/edit.html",
                  {
                      'title': 'Create new target website',
                      'is_secretkey_insecure': is_secretkey_insecure,
                      'operation': "create",
                  })

@never_cache
@user_passes_test(staff_privilege_check)
def websites_edit(request, website_id):

    the_website = get_object_or_404( models.TargetWebsite, id=website_id )

    return render(request, "panel/websites/edit.html",
                  {
                      'title': 'Website edit',
                      'is_secretkey_insecure': is_secretkey_insecure,
                      'operation': "edit",
                      'the_website' : the_website,
                  })


@api_view(['GET', 'POST', ])
@authentication_classes((SessionAuthentication,))
@permission_classes((IsOperatorAuthenticated,))
def api_uptime_list(request):
    results = []

    for s in models.TargetWebsite.objects.order_by('url', ):
        try:
            previous_exception_ = models.UptimeCheck.objects.filter(target_website=s,
                                                                    status__in=['error', 'exception',
                                                                                'missing_keyword']).order_by(
                '-start_time', )[0]

            previous_exception = {
                'time': previous_exception_.end_time.timestamp(),
                'status': previous_exception_.status,
                'status_display': previous_exception_.get_status_display()
            }
        except:
            previous_exception = None
            previous_exception_display = None

        # models.UptimeCheck.objects.
        uptimes = []
        for u in models.UptimeCheck.objects.filter(target_website=s).order_by('-start_time', )[:5]:
            uptimes.append({
                'id': u.id,
                'status': u.status,
                'status_code': u.status_code,
                'status_display': u.get_status_display(),
                'end_time_display': f'{u.end_time}',
                'end_time': u.end_time.timestamp() if u.end_time else None,
            })
        timestamp = None
        if s.ssl_expire_time:
            timestamp = s.ssl_expire_time.timestamp()

        results.append({
            'id': f'{s.id}',
            'title': s.title,
            'target_website_url': f'{s.url}',
            'ssl_expire_time': timestamp,
            'uptimes': uptimes,
            'previous_exception': previous_exception,
        })

    return JsonResponse({
        'objects': results,
        'status': 'okay'
    })


@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsOperatorAuthenticated,))
def api_trigger_refresh(request):
    if settings.DEBUG:
        print(f"{colorama.Fore.RED}request user is:{colorama.Style.RESET_ALL} {request.user.username}")

    if "mode" in request.data and request.data["mode"]:
        if request.data["mode"] == "all":
            check_domains()

            message = "Refresh all triggered"

            return JsonResponse({
                'message': message,
                'status': 'okay'
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
                'message': message,
                'status': 'okay'
            })

    return JsonResponse({
        'error': "Invalid trigger request",
        'status': 'error'
    })

@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_users_list(request):
    objects = []
    for user in User.objects.all():
        objects.append({
            'id' : user.id,
            'username' : user.username,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'role' : user.role,

            'role_display' : user.get_role_display(),
            'is_staff': user.is_staff,
            'date_joined' : user.date_joined.timestamp() if user.date_joined else None,
        })

    return JsonResponse({
        'status' : 'okay',
        'objects' : objects,
    })

@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_users_read(request):
    f = forms.ReadUserForm(request.data)
    if f.is_valid():
        the_user = User.objects.get(id=f.cleaned_data['user_id'])

        d = {
        }
        for field in ['username', 'first_name', 'last_name', 'role', 'email', 'id']:
            d[field] = getattr( the_user, field )
        if settings.DEBUG:
            print(d)
        return JsonResponse({
            'status' : 'okay',
            'object' : d
        })
    else:
        return JsonResponse({
            'status' : 'error',
            'error' : 'Invalid user ID'
        })

@api_view(['GET', 'POST', ])
def api_users_first_time_setup(request):
    if settings.DEBUG:
        f = forms.FirstTimeSuperuserRegistrationForm(request.data)
        if f.is_valid():
            # only add if there is really no user?
            if not first_run_has_no_users():
                return JsonResponse({
                    'status' : 'error',
                    'error' : 'There is already a super user registered.'
                })

            the_user = User.objects.create_user(f.cleaned_data['username'], f.cleaned_data["email"],
                                                    f.cleaned_data["password"])
            the_user.first_name = f.cleaned_data["first_name"]
            the_user.last_name = f.cleaned_data["last_name"]
            the_user.role = "admin"
            the_user.is_staff = True
            the_user.save()

            try:
                the_user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, the_user)
            except Exception as inst:
                print(type(inst))  # the exception instance
                print(inst.args)  # arguments stored in .args
                print(inst)  # __str__ allows args to printed directly

            return JsonResponse({
                'status': 'okay',
            })
        else:
            form_errors = {}
            for e in f.errors.items():
                print(e)
                form_errors[e[0]] = e[1][0]

            if settings.DEBUG:
                print(f'{colorama.Fore.RED}not f.is_valid(){colorama.Style.RESET_ALL}')
                print(form_errors)

            return JsonResponse({
                'status': 'error',
                'form_errors': form_errors,
                'error': "Form not valid",
            })


    else:
        return JsonResponse({
            'status' : 'error',
            'error' : 'First time setup is no longer available if it is not in DEBUG mode'
        })
@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_users_edit(request):
    if request.data["operation"] == "edit":
        f = forms.EditUserForm(request.data)
    else:
        f = forms.AddUserForm(request.data)

    if f.is_valid():
        if f.cleaned_data["operation"] not in ["edit", "create"]:
            return JsonResponse({
                'status' : 'error',
                'error' : 'Invalid operation'
            })

        # if operation is "create"
        if f.cleaned_data["operation"] == "edit":
            try:
                the_user = User.objects.get(id=f.cleaned_data["id"])
            except:
                return JsonResponse({
                    'status' : 'error',
                    'error' : "User does not exist"
                })
        else:
            the_user = User.objects.create_user( f.cleaned_data['username'], f.cleaned_data["email"], f.cleaned_data["password"])
        the_user.first_name = f.cleaned_data["first_name"]
        the_user.last_name = f.cleaned_data["last_name"]
        the_user.role = f.cleaned_data["role"]
        if the_user.role == "admin":
            the_user.is_staff = True
        the_user.save()

        return JsonResponse({
            'status': 'okay',
            #'objects' : objects,
        })

    else:
        form_errors = {}
        for e in f.errors.items():
            print(e)
            form_errors[ e[0] ] = e[1][0]

        if settings.DEBUG:
            print(f'{colorama.Fore.RED}not f.is_valid(){colorama.Style.RESET_ALL}')
            print( form_errors )


        return JsonResponse({
            'status': 'error',
            'form_errors': form_errors,
            'error': "Form not valid",
        })


@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_users_delete(request):
    f = forms.DeleteUserForm( request.data )
    if f.is_valid():
        the_user = User.objects.get(id=f.cleaned_data["user_id"])
        if the_user == request.user:
            return JsonResponse({
                'status': 'error',
                'error': 'You cannot delete the current user'
            })

        the_user.delete()

        return JsonResponse({
            'status' : 'okay',
        })
    else:
        return JsonResponse({
            'status': 'error',
            'error' : 'Invalid User ID'
        })

@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_users_reset_password(request):
    f = forms.ResetPasswordForm(request.data)
    if f.is_valid():
        the_user = User.objects.get(id=f.cleaned_data["user_id"])
        the_user.set_password(f.cleaned_data["new_password"])
        the_user.save()

        return JsonResponse({
            'status': 'okay',
        })
    else:
        form_errors = {}
        for e in f.errors.items():
            print(e)
            form_errors[e[0]] = e[1][0]

        if settings.DEBUG:
            print(f'{colorama.Fore.RED}not f.is_valid(){colorama.Style.RESET_ALL}')
            print(form_errors)

        return JsonResponse({
            'status': 'error',
            'form_errors': form_errors,
            'error': "Form not valid",
        })

@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsOperatorAuthenticated,))
def api_users_change_password(request):
    if settings.DEBUG:
        print(request.data)

    f = forms.ChangePasswordForm(request.data)
    if f.is_valid():
        the_user = request.user
        the_user.set_password(f.cleaned_data["new_password"])
        the_user.save()
    else:
        form_errors = {}
        for e in f.errors.items():
            print(e)
            form_errors[e[0]] = e[1][0]

        if settings.DEBUG:
            print(f'{colorama.Fore.RED}not f.is_valid(){colorama.Style.RESET_ALL}')
            print(form_errors)

        return JsonResponse({
            'status': 'error',
            'form_errors': form_errors,
            'error': "Unable to change password",
        })


@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_websites_read(request):
    f = forms.ReadWebsiteForm(request.data)
    if f.is_valid():
        the_website = models.TargetWebsite.objects.get(id=f.cleaned_data['website_id'])

        d = {
        }
        for field in ['title', 'url', 'must_contain_keyword', 'flag_cdn_random_key', 'flag_check_ssl_expire_time', 'flag_notify_email_downtime', 'flag_notify_slack_downtime', 'id']:
            d[field] = getattr(the_website, field)
        if settings.DEBUG:
            print(d)
        return JsonResponse({
            'status': 'okay',
            'object': d
        })
    else:
        return JsonResponse({
            'status': 'error',
            'error': 'Invalid website ID'
        })
@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_websites_edit(request):
    f = forms.EditWebsiteForm(request.data)

    if f.is_valid():
        if f.cleaned_data["operation"] not in ["edit", "create"]:
            return JsonResponse({
                'status': 'error',
                'error': 'Invalid operation'
            })

        # if operation is "create"
        if f.cleaned_data["operation"] == "edit":
            try:
                the_website = models.TargetWebsite.objects.get(id=f.cleaned_data["id"])
            except:
                return JsonResponse({
                    'status': 'error',
                    'error': "Website does not exist"
                })
        else:
            the_website = models.TargetWebsite()
        for field in f.fields:
            if field not in ["operation", "id"]:
                setattr(the_website, field, f.cleaned_data[field])
        the_website.save()

        return JsonResponse({
            'status': 'okay',
            # 'objects' : objects,
        })

    else:
        form_errors = {}
        for e in f.errors.items():
            print(e)
            form_errors[e[0]] = e[1][0]

        if settings.DEBUG:
            print(f'{colorama.Fore.RED}not f.is_valid(){colorama.Style.RESET_ALL}')
            print(form_errors)

        return JsonResponse({
            'status': 'error',
            'form_errors': form_errors,
            'error': "Form not valid",
        })

@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_websites_delete(request):
    f = forms.DeleteWebsiteForm( request.data )
    if f.is_valid():
        the_website = models.TargetWebsite.objects.get(id=f.cleaned_data["website_id"])
        the_website.delete()

        return JsonResponse({
            'status' : 'okay',
        })
    else:
        return JsonResponse({
            'status': 'error',
            'error' : 'Invalid Website ID'
        })

@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_test_slack(request):
    f = forms.SlackTestForm(request.data)
    if f.is_valid():
        response = Slack.postMessage( settings.SLACK_ROOM, f.cleaned_data["message"])

        if not response:
            return JsonResponse({
                'status' : 'error',
                'error' : "Unable to get a response from Slack"
            })
        else:
            return JsonResponse({
                'status' : 'okay',
            })
    else:
        return JsonResponse({
            'status': 'error',
            'error' : 'Form is error'
        })

@api_view(['GET', 'POST', ])
# @authentication_classes((JWTAuthentication, SessionAuthentication))
@authentication_classes((SessionAuthentication,))
@permission_classes((IsStaffAuthenticated,))
def api_test_email(request):
    f = forms.EmailTestForm(request.data)
    if f.is_valid():
        try:
            send_mail(
                "Test e-mail from Uptime Checker",
                "Test e-mail generated on %s" % timezone.now(),
                settings.SERVER_EMAIL,
                [f.cleaned_data['email']],
                fail_silently=False,
            )
        except:
            return JsonResponse({
                'status': 'error',
                'error': "Unable to send e-mail"
            })
        else:
            return JsonResponse({
                'status': 'okay',
            })
    else:
        return JsonResponse({
            'status': 'error',
            'error': 'Form is error'
        })


def first_run_superuser_setup(request):
    return render( request, "panel/users/first_time_setup.html", {

    })

@never_cache
@user_passes_test(operator_privilege_check)
def logout_(request):
    logout(request)

    return HttpResponseRedirect("/")  # reverse("landing:index")
