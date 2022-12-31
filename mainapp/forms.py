from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from captcha.fields import CaptchaField
from .models import *


class AddNewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].empty_label = "Категорія не вибрана"

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Error > 200 chars')
        return title
    # title = forms.CharField(max_length=255, label="Назва", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Текст")
    # # photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    # is_published = forms.BooleanField(label="Публікувати", required=False, initial=True)
    # categories = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категорії", empty_label="Категорія не вибрана")


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label="Ім'я", max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()

