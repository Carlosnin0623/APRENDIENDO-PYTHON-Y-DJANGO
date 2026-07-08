from django.shortcuts import render
from django.http import HttpResponse

from datetime import date

# Create your views here.
def home(request):
    today = date.today()
    stack = ['Python', 'Django','Goolang', 'PHP', 'JS']
    return render(request,'landing/landing.html', {
        'name': 'Ricardo',
        'age': 28,
        'today': today,
        'stack': stack
    })
    
def stack_detail(request):
    pass