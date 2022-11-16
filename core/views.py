from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def biography(request):
    return render(request, "core/biography.html")


def gallery(request):
    return render(request, "core/gallery.html")


def contact(request):
    return render(request, "core/contact.html")
