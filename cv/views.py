from django.shortcuts import render
from .models import Profile
# Create your views here.

def landing(request):
    return render(request, 'landing.html')
