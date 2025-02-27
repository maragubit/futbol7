from django.shortcuts import render
from .models import Partido

# Create your views here.
def partidos(request):
    partidos=Partido.objects.all().order_by('-fecha')
    return render (request,'partidos.html',{'partidos':partidos})