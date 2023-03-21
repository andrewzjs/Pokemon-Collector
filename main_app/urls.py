from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("pokemon/", views.pokemon_index, name="pokemon"),
    path("pokemon/<int:p_id>/", views.pokemon_detail, name="pokemon_detail"),
    path("pokemon/create", views.PokemonCreate.as_view(), name="pokemon_create"),
    path("pokemon/<int:pk>/update/", views.PokemonUpdate.as_view(), name="pokemon_update"),
    path("pokemon/<int:pk>/delete/", views.PokemonDelete.as_view(), name="pokemon_delete"),
]
