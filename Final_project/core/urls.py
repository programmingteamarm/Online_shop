from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('brand/', views.brand, name='brand'),
    path('contact/', views.contact, name='contact')
]
