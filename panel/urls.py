#from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name="index" ),
    path('configurations/', views.configurations, name="configurations"),
    path('users/', views.users, name="users"),
    path('users/create/', views.users_create, name="users_create"),
    path('users/edit/<int:user_id>/', views.users_edit, name="users_edit"),

    path('website/create/', views.websites_create, name="websites_create"),
    path('website/edit/<uuid:website_id>/', views.websites_edit, name="websites_edit"),

    # APIs for listing uptimes
    path('api/uptime-list/', views.api_uptime_list, name="api_uptime_list"),
    path('api/trigger-refresh/', views.api_trigger_refresh, name="api_trigger_refresh"),

    # APIs for users
    path('api/users/list/', views.api_users_list, name="api_users_list"),
    path('api/users/read/', views.api_users_read, name="api_users_read"),

    path('api/users/edit/', views.api_users_edit, name="api_users_edit"),
    path('api/users/delete/', views.api_users_delete, name="api_users_delete"),

    path('api/websites/read/', views.api_websites_read, name="api_websites_read"),
    path('api/websites/edit/', views.api_websites_edit, name="api_websites_edit"),
    path('api/websites/delete/', views.api_websites_delete, name="api_websites_delete"),



    # Logout
    path('logout/', views.logout, name="logout"),

]
