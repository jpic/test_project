from django.contrib import admin

from models import *


class YAdmin(admin.ModelAdmin):
    list_filter = ('x',)

admin.site.register(Y, YAdmin)
admin.site.register(X)

