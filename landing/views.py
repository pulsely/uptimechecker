from django.shortcuts import render

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from django.conf import settings
from django.views.decorators.cache import never_cache

@never_cache
def index(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect( reverse( settings.URL_POST_SIGNIN ))

    return render( request, "landing/index.html",
                              {
                                  'SAAS_TEMPLATE_STYLE' : 'navbar-white-header',
                                  'flag_nav_spacer': True
                              })
