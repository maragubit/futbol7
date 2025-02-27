from django.shortcuts import render
from .models import Equipo
from .models import Jugador
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
# Create your views here.
def convocatoria(request):
    equipos=Equipo.objects.all().order_by("-fecha")[:2]
    equipo_local=equipos[0]
    equipo_visitante=equipos[1]
    return render (request,'convocatoria.html',{'equipo_local':equipo_local,'equipo_visitante':equipo_visitante})

def create (request):
    jugadores=Jugador.objects.all()
    return render (request,'createTeamExpress.html',{'jugadores':jugadores})

def store(request):
    if request.method == "POST":
        jugadores_ids = request.POST.getlist('jugadores')  # Obtener lista de IDs seleccionados
        jugadores = list(Jugador.objects.filter(id__in=jugadores_ids))
        jugadores = sorted(jugadores, key=lambda j: j.puntos(), reverse=True)
        for jugador in jugadores:
            print(jugador)
        if len(jugadores) < 2:
            return redirect('/admin/')  # Si no hay suficientes jugadores, redirigir

        else:
            equipo_local = Equipo.objects.create(color="Blanco")
            equipo_local.save()
            equipo_visitante = Equipo.objects.create(color="Color")  # Puedes cambiar el color
            equipo_visitante.save()

            for index, jugador in enumerate(jugadores):
                if index % 2 == 0:
                    equipo_local.jugadores.add(jugador)  # Jugador al equipo local
                else:
                    equipo_visitante.jugadores.add(jugador)  # Jugador al equipo visitante

        return redirect('/admin/')

    return redirect('admin')

            

        

    return redirect(request, "admin")

# Create your views here.

class EquipoDetailView(DetailView):

    model = Equipo
    template_name="equipo.html"