from django.shortcuts import render
from django.http import HttpResponse


def etusivu(request):
    return HttpResponse('Autokorjaamo')

