from django import forms
from .models import Blogs
from django.forms import widgets

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }