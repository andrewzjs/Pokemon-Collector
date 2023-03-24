from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Generic URLs
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("accounts/signup/", views.signup, name="signup"),
    # Pokemon URLs
    path("pokemon/", views.pokemon_index, name="pokemon"),
    path("pokemon/<int:p_id>/", views.pokemon_detail, name="pokemon_detail"),
    path("pokemon/create", views.PokemonCreate.as_view(), name="pokemon_create"),
    path("pokemon/<int:pk>/update/", views.PokemonUpdate.as_view(), name="pokemon_update"),
    path("pokemon/<int:pk>/delete/", views.PokemonDelete.as_view(), name="pokemon_delete"),
    # Feeding URLs
    path("pokemon/<int:pokemon_id>/add_feeding/", views.add_feeding, name="add_feeding"),
    # Toys URLs
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('pokemon/<int:p_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]
