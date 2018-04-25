from django.contrib import admin

# Register your models here.
from .models import Ad, Campaign, Device

admin.site.register(Ad)
admin.site.register(Campaign)
admin.site.register(Device)
