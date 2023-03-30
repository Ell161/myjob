from django.contrib import admin
from .models import *


@admin.register(UserNationality)
class UserNationalityAdmin(admin.ModelAdmin):
    list_display = ('id', "nationality", )


@admin.register(MainInfoResume)
class MainInfoResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name', 'birthday',
                    'gender', 'city', 'email', 'phone', 'nationality', 'date_create', 'is_published', )
