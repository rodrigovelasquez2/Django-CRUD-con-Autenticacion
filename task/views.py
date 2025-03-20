from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    # form se usa en HTML
    return render(request, 'home.html')


def signup(request):
    # form se usa en HTML
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })