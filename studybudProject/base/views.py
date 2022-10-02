from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

# Create your views here.




def home(request):
    return render(request, 'base/home.html')


def room(request, name):
    
    context={'name':name}
    return render(request, 'base/room.html', context)