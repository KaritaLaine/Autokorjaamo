from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import *



def palvelut(request):
    palvelut = Palvelu.objects.all()
    context = {'palvelut' : palvelut}
    return render(request, 'autokorjaamo/palvelut.html',context)