from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import Group

from .forms import RegisterUserForm


class RegisterApplicantView(CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        user = form.save()
        group = Group.objects.get(name='Applicants')
        user.groups.add(group)
        if user:
            login(self.request, user)

        return super(RegisterApplicantView, self).form_valid(form)
