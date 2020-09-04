from django.shortcuts import render #render returns an HTML file as HttpResponse
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
        
    if request.GET.get('specialchars'):
        characters.extend(list('!@#$%^&*()/}{[]\><.,?_-+='))
    
    length = int(request.GET.get('length', 8)) #8 is the default length of password
    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)
        
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')