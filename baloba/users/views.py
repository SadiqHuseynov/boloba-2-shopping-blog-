from django.shortcuts import render
from .models import UserProfile
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your views here.

User = get_user_model()

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username = form.cleaned_data.get('email'),
                email = form.cleaned_data.get('email'),
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name') 
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            user_profile = UserProfile.objects.create(
                user = user,
                user_type = form.cleaned_data.get('user_type'),
                about = form.cleaned_data.get('about'),
            )
            messages.success(request, 'User registered successfully :)')
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form})  

def login_user(request):
    form = UserRegisterForm()
    return render(request, 'login.html', {'form': form})

def my_account(request):
    return render(request, 'my-account.html')          