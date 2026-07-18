# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render

# Create your views here.
def index(request):
    
    days = list(days_of_week.keys())

    return render(request, 'quotes/index.html', {
        "days": days
    })

""" 
def monday(request):
    return HttpResponse("Hola Lunes")

def tuesday(request):
    return HttpResponse("Hola Martes")

"""

days_of_week = {
    "monday": "Pienso, Luego existo",
    "tuesday": "La vida es un sueño",
    "wednesday": "El conocimiento es poder",
    "thursday": "Sé el cambio que quieres ver",
    "friday": "Solo sé que no sé nada",
    "saturday": "Vive como si fuera la último día",
    "sunday": "Da un poquito más todos los días"
}

    
def days_week_with_number(request, day):
    days = list(days_of_week.keys())
        
    if day > len(days):
        return HttpResponseNotFound("El día no existe")
    
    redirect_day = days[day - 1]
    
    redirect_path = reverse("day-quote", args=[redirect_day])

    return HttpResponseRedirect(redirect_path)

def days_week(request, day):
    try:
     quote_text = days_of_week[day]
     return HttpResponse(quote_text)
    except Exception:
     # return HttpResponseNotFound("Este día no existe")
     return render(request, "./includes/404.html")
     raise Http404() # Esto generara el error 404 pero ya en producción y buscara automaticamente el archivo 404.html
     # Pero por ahora usa el render para hacer pruebas con el archivo
    