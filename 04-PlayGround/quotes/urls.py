from django.urls import path
from . import views

 # Rutas estaticas en Django
urlpatterns = [
    path("", views.index),
    # path("monday", views.monday),
    #path("tuesday", views.tuesday),
    path("<int:day>", views.days_week_with_number), # Ruta dinamica en python van dentro de estos simbolos <day>
    path("<str:day>", views.days_week, name="day-quote"),
]
