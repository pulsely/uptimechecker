from django.shortcuts import render

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import user_passes_test
from uptimecheckcore.components.credentials.privileges import operator_privilege_check, IsOperatorAuthenticated

@never_cache
@user_passes_test(operator_privilege_check)
def index(request):
    return render(request, "help/index.html",
                  {
                      'title': 'Help',
                  })
