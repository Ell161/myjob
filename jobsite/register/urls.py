from django.urls import path
from .views import *

app_name = 'register'
urlpatterns = [
    path('', RegisterApplicantView.as_view(), name='register'),
]