from django.shortcuts import render
from .models import Biography

# Create your views here.


def biography(request):
    events = Biography.objects.all()
    return render(request, "biography/biography.html", {'events': events})
