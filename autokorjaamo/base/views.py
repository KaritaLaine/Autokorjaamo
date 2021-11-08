from django.shortcuts import render
from .forms import PalauteLomake
from django.http import HttpResponseRedirect
from .models import Palvelu

def etusivu(request):
    return render(request, 'etusivu.html')

def palvelut(request):
    palvelut = Palvelu.objects.all()
    context = {'palvelut' : palvelut}
    return render(request, 'palvelut.html', context)

def yhteystiedot(request):
    return render(request, 'yhteystiedot.html')

def palaute(request):
    return render(request, 'palaute.html')

def asiakaspalaute(request):
    submitted = False
    if request.method == 'POST':
        form = PalauteLomake(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/palautelomake?submitted=True')
    else:
        form = PalauteLomake
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'palautelomake.html', {'form':form, 'submitted':submitted})