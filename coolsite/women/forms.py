from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from users.models import CustomUser
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField, CaptchaTextInput

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'author']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'content']
        widgets = {
            'email': forms.EmailInput,
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }


class RegisterUserForm(UserCreationForm):
    # username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'fio', 'gender', 'birth_date', 'ava', 'slug', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'fio', 'gender', 'birth_date', 'ava')


class LoginAjaxForm(forms.Form):
    username = forms.CharField(
        label='Логин',
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'username',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control'
            }
        )
    )


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'autocomplete': 'username',
            'class': 'form-control'
            }
        )
    )
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'autocomplete': 'current-password',
            'class': 'form-control'
            }
        )
    )


class ContactForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField(label="Капча")
