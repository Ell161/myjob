from django import forms
from .models import *


class MainInfo(forms.ModelForm):
    class Meta:
        model = MainInfoResume
        fields = ['photo', 'last_name', 'first_name', 'middle_name',
                  'birthday', 'gender', 'city', 'email', 'phone',
                  'nationality', 'is_published']

        labels = {
            'photo': 'Фотография*',
            'last_name': 'Фамилия*',
            'first_name': 'Имя*',
            'middle_name': 'Отчество',
            'birthday': 'Дата рождения*',
            'gender': 'Пол*',
            'city': 'Город проживания*',
            'email': 'Email*',
            'phone': 'Телефон*',
            'nationality': 'Гражданство*',
            'is_published': 'Опубликовать*'
        }