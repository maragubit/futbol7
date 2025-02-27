from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Jugador

# Create your views here.

class JugadorDetailView(DetailView):

    model = Jugador
    template_name="jugador.html"