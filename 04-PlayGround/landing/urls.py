from django.urls import path
from . import views

 # Rutas estaticas en Django
urlpatterns = [
    path("home", views.home),
]
