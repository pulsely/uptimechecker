"""
uptimechecker URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
import os



urlpatterns = [
    path('', include('landing.urls')),
    path('panel/', include('panel.urls')),
    path('help/', include('help.urls')),

    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='panel/login.html', extra_context={
        'NAVBAR_STYLE': 'navbar-white'
    }), name="account_login"),
]
if settings.DEBUG:
    from django.conf.urls.static import static

    #urlpatterns += static('media/', document_root=os.path.join(settings.BASE_DIR, 'src/media'))
    urlpatterns += static('lookandfeel/', document_root=os.path.join(settings.BASE_DIR, 'src/lookandfeel/'))
    urlpatterns += static('static/', document_root=os.path.join(settings.BASE_DIR, 'src/static/'))

admin.site.site_header = "Uptime Checker by Pulsely"
admin.site.index_title = "Admin Console"
admin.site.site_title = "Uptime Checker by Pulsely"

