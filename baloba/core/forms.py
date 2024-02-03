from django import forms
from django.forms import widgets
from core.models import Subscriber

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(label='E-Mail Address', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    message = forms.CharField(label='Enquiry',widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email' : widgets.EmailInput(attrs={'class': 'input-text required-entry validate-email', 'placeholder': 'Email'}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already in use')
        return email    