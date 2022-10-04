from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Room
from .forms import RoomForm

# Create your views here.



def home(request):
    return render(request, 'base/home.html')


def room(request, name):
    
    context={'name':name}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form=RoomForm()
    # if request.method=='POST':
    #     form=RoomForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return 'hello'
    context={'form':form}
    return render(request, 'base/room-form.html', context)