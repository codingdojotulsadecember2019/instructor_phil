from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
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
        result_from_model = Planet.objects.validate_planet(request.POST)
        print(result_from_model)
        if result_from_model[0] == True:
            new_planet = Planet.objects.create(name=request.POST['name'], size=request.POST['size'])
            print(new_planet.id)
            return redirect(f'/planets/{ new_planet.id }')
        else:
            #handle errors
            print(result_from_model[1])
            for error in result_from_model[1]:
                print(error)

                messages.error(request, error)

            return redirect('/planets/new')


def new(request):
    return render(request, 'first_app/new.html')

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