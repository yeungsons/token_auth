from django.contrib import admin as dadmin
from django.contrib.auth.models import User
from admin import CustomUserAdmin

dadmin.site.unregister(User)
dadmin.site.register(User, CustomUserAdmin)