"""
URL configuration for futbol7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home,clasificacion
from jugadores.views import JugadorDetailView
from equipos.views import convocatoria,EquipoDetailView
from partidos.views import partidos
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('clasificacion', clasificacion, name="clasificacion"),
    path("jugador/<int:pk>",JugadorDetailView.as_view(), name="jugador"),
    path('convocatoria',convocatoria, name="convocatoria"),
    path('partidos',partidos, name="partidos"),
    path("equipo/<int:pk>",EquipoDetailView.as_view(), name="equipo"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
