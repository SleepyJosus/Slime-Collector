from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Slime

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def slimes_index(request):
    slimes = Slime.objects.all()
    return render(request, 'slimes/index.html', {'slimes': slimes})

def slimes_detail(request, slime_id):
    slime = Slime.objects.get(id=slime_id)
    return render(request, 'slimes/detail.html', {'slime': slime})

class SlimeCreate(CreateView):
    model = Slime
    fields = '__all__'

class SlimeUpdate(UpdateView):
    model = Slime
    fields = ['breed', 'description', 'age']

class SlimeDelete(DeleteView):
    model = Slime
    success_url = '/slimes/'