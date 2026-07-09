from django.shortcuts import render
from django.http import HttpResponse

from datetime import date

# Create your views here.
def home(request):
    today = date.today()
   # stack = ['Python', 'Django','Goolang', 'PHP', 'JS']
    stack = [
            {'id':'python','name':'Python'},
            {'id':'django','name':'Django'},
            {'id':'goolang','name':'Goolang'},
            {'id':'php','name':'PHP'},
            {'id':'js','name':'JS'}
            ]
    return render(request,'landing/landing.html', {
        'name': 'Ricardo',
        'age': 28,
        'today': today,
        'stack': stack
    })
    
def stack_detail(request, tool):
    return HttpResponse(f"Tecnología: {tool}")