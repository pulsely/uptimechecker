#from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name="index" ),
    path('settings/', views.settings_, name="settings"),
    path('users/', views.users, name="users"),

    path('api/uptime-list/', views.api_uptime_list, name="api_uptime_list"),

    path('api/trigger-refresh/', views.api_trigger_refresh, name="api_trigger_refresh"),

]
