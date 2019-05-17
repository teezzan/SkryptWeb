from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Skrypt
# Register your models here.


class MyAdminSite(AdminSite):
    site_header = 'Skrypt Administration'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Skrypt)
admin.register(Skrypt)