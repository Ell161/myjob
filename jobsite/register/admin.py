from django.contrib import admin
from django.contrib.auth.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'last_name', 'first_name', 'email', 'is_active', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
