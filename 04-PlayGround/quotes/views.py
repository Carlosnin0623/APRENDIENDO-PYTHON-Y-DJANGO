from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo desde Django!")

""" 
def monday(request):
    return HttpResponse("Hola Lunes")

def tuesday(request):
    return HttpResponse("Hola Martes")

"""
def days_week(request, day):
    quote_text = None
    
    if day.lower() == "monday":
        quote_text = "Pienso, Luego existo"
        
    elif day.lower() == "tuesday":
        quote_text = "La vida es un sueño"
    else:
        return HttpResponseNotFound("No hay frase para este día.")
    
    return HttpResponse(quote_text)
        
        
    