from django.shortcuts import render

def etusivu(request):
    return render(request, 'etusivu.html')

def palvelut(request):
    return render(request, 'palvelut.html')

def yhteystiedot(request):
    return render(request, 'yhteystiedot.html')

def palaute(request):
    return render(request, 'palaute.html')

