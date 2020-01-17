from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('planets', views.create),
    path('planets/<int:planet_id>', views.show),
    path('moons/<int:planet_id>', views.create_moon)
]
