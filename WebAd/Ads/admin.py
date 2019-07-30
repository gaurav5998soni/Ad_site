from django.contrib import admin
from .models import Profile, AdUnit, TextAd, ImageAd, Tags

admin.site.register(Profile)
admin.site.register(AdUnit)
admin.site.register(TextAd)
admin.site.register(ImageAd)
admin.site.register(Tags)
