from django.shortcuts import render

from django.http import HttpResponse
from .models import Slime

# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def about(request):
    return render(request, 'about.html')

def slimes_index(request):
    slimes = Slime.objects.all()
    return render(request, 'slimes/index.html', {'slimes': slimes})

def slimes_detail(request, slime_id):
    slime = Slime.objects.get(id=slime_id)
    return render(request, 'slimes/detail.html', {'slime': slime})