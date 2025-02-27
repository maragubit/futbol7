from django.shortcuts import render
from .models import Equipo
from django.views.generic.detail import DetailView

# Create your views here.
def convocatoria(request):
    equipos=Equipo.objects.all().order_by("-fecha")[:2]
    equipo_local=equipos[0]
    equipo_visitante=equipos[1]
    return render (request,'convocatoria.html',{'equipo_local':equipo_local,'equipo_visitante':equipo_visitante})

# Create your views here.

class EquipoDetailView(DetailView):

    model = Equipo
    template_name="equipo.html"