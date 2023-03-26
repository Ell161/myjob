from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse

from .forms import *


def create_main_info(request: HttpRequest):
    header = [('index.html', 'MyJob'),
              ('index.html', 'Вакансии'),
              ('index.html', 'Резюме'),
              ('index.html', 'Личный кабинет')]
    if request.method == "POST":
        form = MainInfo(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("resume:desired_position")
            return redirect(url)
    else:
        form = MainInfo()

    context = {'headers': header,
               'form': form}
    return render(request, 'resume/create.html', context=context)