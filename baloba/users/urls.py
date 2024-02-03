from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('my_account/', views.my_account, name="my_account")
]

 