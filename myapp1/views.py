from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal
# Create your views here.
def view(request):
    animals = Animal.objects.all()
    return render(request, 'myapp1/home.html', {'animals': animals})