from django.contrib import admin
from .models import *


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(Vacation)
class SVacationAdmin(admin.ModelAdmin):
    fields = ('title', 'specialization', )
