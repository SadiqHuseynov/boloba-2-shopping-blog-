from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(forms.Form):
    email = forms.EmailField(label='Email address:', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='Password:',widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password_confirmation = forms.CharField(label='Password confirmation:', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    first_name = forms.CharField(label='First name:', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(label='Last name: ', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    about = forms.CharField(label='About', widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    user_type = forms.ChoiceField(label='User type:', choices=[(1, 'Viewer'), (2, 'Publisher')], widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        checking_mail = User.objects.filter(email=email)
        if checking_mail.exists():
            raise forms.ValidationError('This Email is exists!')
        return email
    
    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Passwords dont match')
        return self.cleaned_data
    
# class UserLoginForm(forms.Form):
#     email = forms.EmailField(label='Email address:', widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     password = forms.CharField(label='Password:',widget=forms.PasswordInput(attrs={
#         'class': 'form-control'
#     }))
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         checking_mail = User.objects.filter(email=email)
#         if not checking_mail.exists():
#             raise forms.ValidationError("E-mail is not registered!")
#         return email
    
#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         email = self.cleaned_data.get('email')
#         user = User.objects.filter(email=email).first()
#         if user:
#             if not user.check_password(password):
#                 raise forms.ValidationError('Password is incorret')
#         return data    