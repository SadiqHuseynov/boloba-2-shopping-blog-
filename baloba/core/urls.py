from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('search/', views.search_product, name="search_product")
]
 