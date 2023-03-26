from django.urls import path
from .views import *

app_name = 'resume'
urlpatterns = [
    path('create/', create_main_info, name='create'),
]