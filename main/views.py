from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })

def terminos(request):
    return render(request, 'terminos.html')

def privacidad(request):
    return render(request, 'terminos.html')