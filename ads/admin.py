from django.contrib import admin

# Register your models here.
from .models import Ad, Device

admin.site.register(Ad)
admin.site.register(Device)
