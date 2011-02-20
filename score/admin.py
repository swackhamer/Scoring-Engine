from ccdc.score.models import *
from django.contrib import admin

class serviceAdmin(admin.ModelAdmin):
    pass

class teamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, serviceAdmin)
admin.site.register(Team, teamAdmin)