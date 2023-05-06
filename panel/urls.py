#from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name="index" ),
    path('configurations/', views.configurations, name="configurations"),
    path('users/', views.users, name="users"),

    # APIs for listing uptimes
    path('api/uptime-list/', views.api_uptime_list, name="api_uptime_list"),
    path('api/trigger-refresh/', views.api_trigger_refresh, name="api_trigger_refresh"),

    # APIs for users
    path('api/users/list/', views.api_users_list, name="api_users_list"),
    path('api/users/create/', views.api_users_create, name="api_users_create"),
    path('api/users/delete/', views.api_users_delete, name="api_users_delete"),

    # Logout
    path('logout/', views.logout, name="logout"),

]
