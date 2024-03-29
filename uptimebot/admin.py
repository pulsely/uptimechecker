from django.contrib import admin
from . import models

class UptimeCheckAdmin(admin.ModelAdmin):
    list_display = ('url', 'target_website', 'http_type', 'status', 'start_time', 'end_time', 'status_code', )
    orderings = ('-position',)
    list_filter = ('target_website', 'http_type')

class TargetWebsiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'must_contain_keyword', 'flag_cdn_random_key', 'flag_check_ssl_expire_time', 'ssl_expire_time', 'creation_date' )
    orderings = ('-creation_date',)

admin.site.register(models.UptimeCheck, UptimeCheckAdmin)
admin.site.register(models.TargetWebsite, TargetWebsiteAdmin)
