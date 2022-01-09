from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

admin.site.register(models.Bug)
admin.site.unregister(Group)
admin.site.disable_action('delete_selected')
