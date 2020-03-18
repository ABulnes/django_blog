from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('generals/',generals, name='generales'),
    path('technology/', technology, name='tecnologia'),
    path('programming/', programming, name='programacion'),
    path('games/', games, name='videojuegos'),
    path('tutorials/', tutorials, name='tutoriales'),
    path('<slug:slug>/', detail_post,name='detalle_post')
]