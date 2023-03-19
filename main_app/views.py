from django.shortcuts import render
from django.http import HttpResponse

class Pokemon:
    def __init__(self, name, type, description, age):
        self.name = name
        self.type = type
        self.description = description
        self.age = age

pokemon = [
    Pokemon("Bulbasaur", "grass", "cute little green bulb", 0),
    Pokemon("Pikachu", "electric", " playful yellow electric rat", 3),
    Pokemon("Milotic", "water", "beautiful freshwater eel", 6),
]

# Create your views here.

def home(request):
    return HttpResponse("<h1> Hello!!!! /ᐠ｡‸｡ᐟ\ﾉ </h1>")

def about(request):
    return render(request, "about.html")

def pokemon_index(request):
    return render(request, "pokemon/index.html", {"pokemon": pokemon})