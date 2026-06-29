# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    list_item = ""
    days = list(days_of_week.keys()) # [monday,tuesday,....]

    for day in days:
        day_path = reverse("day-quote", args=[day])
        list_item += f"<li><a href=\"{day_path}\">{day}</a></li>"
    
    response_html = f"<ul>{list_item}</ul>"
    
    return HttpResponse(response_html)

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
    
        
        
    