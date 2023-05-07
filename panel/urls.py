#from django.conf.urls import url
from django.urls import path
from django.conf import settings

from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name="index" ),
    path('configurations/', views.configurations, name="configurations"),
    path('users/', views.users, name="users"),
    path('users/create/', views.users_create, name="users_create"),
    path('users/edit/<int:user_id>/', views.users_edit, name="users_edit"),
    path('users/reset-password/<int:user_id>/', views.users_reset_password, name="users_reset_password"),
    path('users/change-password/', views.change_password, name="change_password"),

    path('website/create/', views.websites_create, name="websites_create"),
    path('website/edit/<uuid:website_id>/', views.websites_edit, name="websites_edit"),

    # APIs for listing uptimes
    path('api/uptime/list/', views.api_uptime_list, name="api_uptime_list"),
    path('api/trigger-refresh/', views.api_trigger_refresh, name="api_trigger_refresh"),

    # APIs for users
    path('api/users/list/', views.api_users_list, name="api_users_list"),
    path('api/users/read/', views.api_users_read, name="api_users_read"),

    path('api/users/first-time-setup/', views.api_users_first_time_setup, name="api_users_first_time_setup"),

    path('api/users/edit/', views.api_users_edit, name="api_users_edit"),
    path('api/users/delete/', views.api_users_delete, name="api_users_delete"),

    path('api/users/reset-password/', views.api_users_reset_password, name="api_users_reset_password"),
    path('api/users/change-password/', views.api_users_change_password, name="api_users_change_password"),

    path('api/websites/read/', views.api_websites_read, name="api_websites_read"),
    path('api/websites/edit/', views.api_websites_edit, name="api_websites_edit"),
    path('api/websites/delete/', views.api_websites_delete, name="api_websites_delete"),

    path('api/test/slack/', views.api_test_slack, name="api_test_slack"),
    path('api/test/email/', views.api_test_email, name="api_test_email"),


    # Logout
    path('logout/', views.logout_, name="logout"),
]


from uptimecheckcore.components.helpers.first_run import first_run_temporary_user_url, first_run_has_no_users
if settings.DEBUG and first_run_has_no_users():
    try:
        urlpatterns += [
            path(f'firsttime/{first_run_temporary_user_url()}/', views.first_run_superuser_setup, name="first_run_superuser_setup"),
        ]
    except:
        pass