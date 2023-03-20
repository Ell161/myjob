from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    header = [('/', 'MyJob'),
              ('index.html', 'Вакансии'),
              ('index.html', 'Резюме'),
              ('index.html', 'Вход'),
              ('index.html', 'Регистрация')]

    resume = [('Название вакансии', 'Специализация', 'Зарплата') for _ in range(8)]
    context = {'headers': header, 'resume': resume}
    return render(request, 'home/index.html', context=context)
