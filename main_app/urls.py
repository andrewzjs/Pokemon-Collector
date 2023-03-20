from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("pokemon/", views.pokemon_index, name="pokemon"),
    path("pokemon/<int:p_id>/", views.pokemon_detail, name="pokemon_detail")
]
