from django.urls import path
from . import views

urlpatterns = [
    path('planets', views.index),
    path('planets/add', views.create),
    path('planets/new', views.new),
    path('planets/<int:planet_id>', views.show),
    path('moons/<int:planet_id>', views.create_moon)
]
