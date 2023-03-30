import datetime
from django import forms
from django.core.exceptions import ValidationError


from .models import *


class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ['photo']

        labels = {
            'photo': 'Фотография',
        }


class MainInfoForm(forms.ModelForm):
    # def __int__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['gender'].empty_label = 'Не выбран'

    class Meta:
        model = MainInfoResume
        fields = ['last_name', 'first_name', 'middle_name',
                  'birthday', 'gender', 'city', 'email', 'phone',
                  'nationality', 'is_published']

        labels = {
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

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'phone': forms.TextInput(attrs={'data-mask': "+7(000)000-00-00"})
        }

    def clean_birthday(self):
        min_date = datetime.date.today() - datetime.timedelta(weeks=52 * 99)
        max_date = datetime.date.today() - datetime.timedelta(weeks=52)

        birthday = self.cleaned_data['birthday']
        if birthday < min_date or birthday > max_date:
            raise ValidationError('Введены данные, превышающие допустимое значение.')
        return birthday

    def clean_last_name(self):
        def valid_symbols(text):
            lower = set('abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+?:"{}[];’')
            return lower.intersection(text.lower()) != set()

        last_name = self.cleaned_data['last_name']
        if len(last_name) > 50:
            raise ValidationError('Введены данные, превышающие допустимое значение.')
        elif valid_symbols(last_name) or not last_name.isalpha():
            raise ValidationError('Введены недопустимые символы.')
        return last_name

    def clean_first_name(self):
        def valid_symbols(text):
            lower = set('abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+?:"{}[];’')
            return lower.intersection(text.lower()) != set()

        first_name = self.cleaned_data['first_name']
        if len(first_name) > 50:
            raise ValidationError('Введены данные, превышающие допустимое значение.')
        elif valid_symbols(first_name) or not first_name.isalpha():
            raise ValidationError('Введены недопустимые символы.')
        return first_name

    def clean_middle_name(self):
        def valid_symbols(text):
            lower = set('abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+?:"{}[];’')
            return lower.intersection(text.lower()) != set()

        middle_name = self.cleaned_data['middle_name']
        if len(middle_name) > 50:
            raise ValidationError('Введены данные, превышающие допустимое значение.')
        elif valid_symbols(middle_name) or not middle_name.isalpha():
            raise ValidationError('Введены недопустимые символы.')
        return middle_name

    def clean_city(self):
        def valid_symbols(text):
            lower = set('abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+?:"{}[];’')
            return lower.intersection(text.lower()) != set()

        city = self.cleaned_data['city']
        if len(city) > 50:
            raise ValidationError('Введены данные, превышающие допустимое значение.')
        elif valid_symbols(city) or not city.isalpha():
            raise ValidationError('Введены недопустимые символы.')
        return city
