from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Toy
from .forms import FeedingForm
# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, "pokemon/index.html", {"pokemon": pokemon})

def pokemon_detail(request, p_id):
    pokemon = Pokemon.objects.get(id=p_id)
    toys_pokemon_doesnt_have = Toy.objects.exclude(id__in=pokemon.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, "pokemon/detail.html", {
        'pokemon': pokemon, 
        "feeding_form": feeding_form,
        'toys': toys_pokemon_doesnt_have
        })

class PokemonCreate(CreateView):
    model = Pokemon
    fields = "__all__"


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = "__all__"

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = "/pokemon/"

def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
    return redirect("pokemon_detail", p_id=pokemon_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, p_id, toy_id):
   c = Pokemon.objects.get(id=p_id)
   c.toys.add(toy_id)
   # OR Toy.objects.get(id=toy_id).cat_set.add(cat_id)
   return redirect(c)