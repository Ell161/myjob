from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(UserCreationForm):
    last_name = forms.CharField(label='', required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    first_name = forms.CharField(label='', required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.EmailField(label='', required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='', required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='', required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'password1', 'password2')

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

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            print("saving user")
            user.save()
        return user
