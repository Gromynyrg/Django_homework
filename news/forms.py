from unicodedata import category

from django.forms import ModelForm, TextInput, DateInput, Textarea
from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date', 'category']
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
                   "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс'}),
                   "date": DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                   "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Статья'})
                   }
