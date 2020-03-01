from django.contrib import admin
from profles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.UserProfileFeed)
