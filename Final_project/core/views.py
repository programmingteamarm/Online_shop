from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def brand(request):
    return render(request, 'core/brand.html')


def contact(request):
    return render(request, 'core/contact.html')
# Create your views here.
