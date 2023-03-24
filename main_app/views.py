from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Toy
from .forms import FeedingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

@login_required
def pokemon_index(request):
    pokemon = Pokemon.objects.filter(user=request.user)
    # OR pokemon = request.user.cat_set.all()
    return render(request, "pokemon/index.html", {"pokemon": pokemon})

@login_required
def pokemon_detail(request, p_id):
    pokemon = Pokemon.objects.get(id=p_id)
    toys_pokemon_doesnt_have = Toy.objects.exclude(id__in=pokemon.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, "pokemon/detail.html", {
        'pokemon': pokemon, 
        "feeding_form": feeding_form,
        'toys': toys_pokemon_doesnt_have
        })

class PokemonCreate(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ['name', 'type', 'description', 'age']

    def form_valid(self, form):
       # Assign the logged in user to the form
       # can find the logged in user in: req.user
       form.instance.user = self.request.user
       return super().form_valid(form)


class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ['name', 'type', 'description', 'age']

class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    success_url = "/pokemon/"

@login_required
def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
    return redirect("pokemon_detail", p_id=pokemon_id)


class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, p_id, toy_id):
   c = Pokemon.objects.get(id=p_id)
   c.toys.add(toy_id)
   # OR Toy.objects.get(id=toy_id).cat_set.add(cat_id)
   return redirect(c)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # Create a user with the data submitted
    # Then, log that user in
    form = UserCreationForm(request.POST)
    if form.is_valid():
       user = form.save()
       # Log that user in
       login(request, user)
       return redirect('pokemon')
    else: 
       error_message = 'Invalid sign up - Try again'
  form = UserCreationForm()
  context = {'form':form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
   