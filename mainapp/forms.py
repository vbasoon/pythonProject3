from django import forms
from django.core.exceptions import ValidationError

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
