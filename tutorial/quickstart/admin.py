from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('api_token',)

    def api_token(self, obj):
        # Example here, you can use any expression.
        return Token.objects.get_or_create(user=obj)[0]

