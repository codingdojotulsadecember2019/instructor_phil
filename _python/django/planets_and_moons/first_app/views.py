from django.shortcuts import render, redirect
from .models import *
# from . import models

# Create your views here.
def index(request):
    all_planets = Planet.objects.all()
    print(all_planets)
    context = {
        'planets': all_planets
    }
    return render(request, 'first_app/index.html', context)

def create(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        Planet.objects.create(name=request.POST['name'], size=request.POST['size'])
    return redirect('/')

def show(request, planet_id):
    print(planet_id)
    planet = Planet.objects.get(id = planet_id)
    print(planet)
    return render(request, 'first_app/show.html', {'one_planet': planet})

def create_moon(request, planet_id):
    # get the planet
    planet = Planet.objects.get(id = planet_id)
    # create the moon with the found planet object
    Moon.objects.create(name=request.POST['name'], planet=planet)
    return redirect('/planets/' + str(planet_id))