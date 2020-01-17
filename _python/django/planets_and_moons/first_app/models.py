from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=55)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<Planet name: { self.name }>'

class Moon(models.Model):
    name = models.CharField(max_length=55)
    planet = models.ForeignKey(Planet, related_name="moons", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
