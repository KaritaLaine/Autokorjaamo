from django.urls import path
from . import views

urlpatterns = [
    path('', views.etusivu, name='etusivu'), 
    path('palvelut/', views.palvelut, name='palvelut'),
    path('yhteystiedot/', views.yhteystiedot, name='yhteystiedot'),
    path('palaute/', views.palaute, name='palaute'),
    path('palautelomake/', views.asiakaspalaute, name='palautelomake')
]