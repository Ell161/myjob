from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import *


def base_resume(request: HttpRequest):
    header = [('index.html', 'MyJob'),
              ('index.html', 'Вакансии'),
              ('index.html', 'Резюме'),
              ('index.html', 'Личный кабинет')]
    context = {'headers': header}
    return render(request, 'resume/base_resume.html', context=context)


def create_main_info(request: HttpRequest):

    if request.method == "POST":
        photo_form = UserPhotoForm(request.POST, request.FILES)
        main_info_form = MainInfoForm(request.POST)
        if main_info_form.is_valid():
            main_info = main_info_form.save()
            file = request.FILES.get('photo')
            resume_photo = UserPhoto.objects.create(photo=file, id_resume=main_info)
            resume_photo.save()
            url = reverse("resume:desired_position")
            return redirect(url)
    else:
        photo_form = UserPhotoForm(request.POST, request.FILES)
        main_info_form = MainInfoForm(request.POST)

    context = {'photo_form': photo_form,
               'main_info_form': main_info_form}
    return render(request, 'resume/create.html', context=context)