from django.contrib import admin
from message import models

class messageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Message, messageAdmin)
