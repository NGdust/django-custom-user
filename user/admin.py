from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    fields = ('name', 'email', 'password', 'is_active', 'is_superuser', 'fb',
              'google_ply', 'game_center', 'tags',)