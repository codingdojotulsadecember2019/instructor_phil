from django.db import models

# Create your models here.
class PlanetManager(models.Manager):
    def validate_planet(self, planet_to_add):
        # validate the form input
        errors = []
        print('+'*50)
        print(planet_to_add['name'])
        print(planet_to_add['size'])
        print('^'*50)
        isValid = True
        if not planet_to_add['name']:
            # name field is empty
            errors.append('Name can not be blank!')
            isValid = False
        if not planet_to_add['size']:
            # size is empty
            errors.append('Must have a size!')
            isValid = False
        return isValid, errors

class Planet(models.Model):
    name = models.CharField(max_length=55)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects - Django's model Manager, to add validations, we will override this
    objects = PlanetManager()

    def __repr__(self):
        return f'<Planet name: { self.name }>'

class Moon(models.Model):
    name = models.CharField(max_length=55)
    planet = models.ForeignKey(Planet, related_name="moons", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
