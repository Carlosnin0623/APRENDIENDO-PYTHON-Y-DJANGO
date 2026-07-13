# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.
def index(request):
    
    days_of_week_2 = [
     {'id': 'monday', 'message': 'Pienso, Luego existo'},
     {'id': 'tuesday', 'message': 'La vida es un sueño'},
     {'id': 'wednesday', 'message': 'El conocimiento es poder'},
     {'id': 'thursday', 'message': 'Sé el cambio que quieres ver'},
     {'id': 'friday', 'message': 'Solo sé que no sé nada'},   
     {'id': 'saturday', 'message': 'Vive como si fuera la último día'},
     {'id': 'sunday', 'message': 'Da un poquito más todos los días'},    
    ]

    return render(request, 'quotes/quotes.html', {
        'days' : days_of_week_2
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


def days_week(request, day):
    try:
     quote_text = days_of_week[day]
     return HttpResponse(quote_text)
    except Exception:
     return HttpResponseNotFound("Este día no existe")
    
def days_week_with_number(request, day):
    days = list(days_of_week.keys())
        
    if day > len(days):
        return HttpResponseNotFound("El día no existe")
    
    redirect_day = days[day - 1]
    
    redirect_path = reverse("day-quote", args=[redirect_day])

    return HttpResponseRedirect(redirect_path)
    