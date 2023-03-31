from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

app_name = 'register'
urlpatterns = [
    path('', RegisterApplicantView.as_view(), name='register'),
    path('login', LoginView.as_view(template_name="register/login.html",
                                    redirect_authenticated_user=True), name='login'),
]