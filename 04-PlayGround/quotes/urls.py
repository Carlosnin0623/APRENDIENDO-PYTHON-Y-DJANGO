from django.urls import path
from . import views

 # Rutas estaticas en Django
urlpatterns = [
    path("hola-mundo", views.index),
    # path("monday", views.monday),
    #path("tuesday", views.tuesday),
    path("<day>", views.days_week), # Ruta dinamica en python van dentro de estos simbolos <day>
]
