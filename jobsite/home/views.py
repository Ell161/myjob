from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    header = [{'link': 'home:index', 'title': 'MyJob'},
              {'link': 'home:index', 'title': 'Вакансии'},
              {'link': 'home:index', 'title': 'Резюме'},
              {'link': 'home:index', 'title': 'Вход'},
              {'link': 'register:register', 'title': 'Регистрация'}]

    resume = [('Название вакансии', 'Специализация', 'Зарплата') for _ in range(8)]
    context = {'headers': header, 'resume': resume}
    return render(request, 'home/index.html', context=context)

