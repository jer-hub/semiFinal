from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):
    persons = Person.objects.all()
    return render(request, 'tracker/index.html',{
        'persons' : persons
    })