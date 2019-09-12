from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Slime, Toy

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
    toys_slime_doesnt_have = Toy.objects.exclude(id__in = slime.toys.all().values_list('id'))
    return render(request, 'slimes/detail.html', {
        'slime': slime,
        'toys': toys_slime_doesnt_have,
        })

class SlimeCreate(CreateView):
    model = Slime
    fields = '__all__'

class SlimeUpdate(UpdateView):
    model = Slime
    fields = ['breed', 'description', 'age']
    
class SlimeDelete(DeleteView):
    model = Slime
    success_url = '/slimes/'

class ToyListView(ListView):
    queryset = Toy.objects.all()

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyDetailView(DetailView):
    queryset = Toy.objects.all()

class ToyUpdateView(UpdateView):
    model = Toy
    fields = ['color']

class ToyDeleteView(DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request, slime_id, toy_id):
    Slime.objects.get(id=slime_id).toys.add(toy_id)
    return redirect('detail', slime_id=slime_id)