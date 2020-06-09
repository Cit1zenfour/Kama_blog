from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserAuthForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')




class CommentForm(forms.ModelForm):
    content = forms.CharField(widget = forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Напишите комментарий',
        'id': 'usercomment',
        'rows': '4',
    }))
    class Meta:
        model = Comment
        fields = ('content',)