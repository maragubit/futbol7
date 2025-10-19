from functools import wraps
from django.utils import timezone

def temporada_default(fn):
    @wraps(fn)
    def wrapper(self, temporada_id=None, *args, **kwargs):
        from partidos.models import Temporada
        # Si se pasa temporada_id, usamos la temporada real
        if temporada_id is not None:
            return fn(self, temporada_id, *args, **kwargs)
        
        
        
        
        else:
            temporada1=Temporada.objects.first()
            temporada2=Temporada().objects.last()
            temporada=Temporada(nombre="Total", inicio=temporada1.inicio, fin=temporada2.fin)
            
        
        # Creamos un objeto de temporada temporal (sin guardar en DB)
        
        
        # Llamamos al método pasando este objeto como "temporada_id"
        return fn(self, temporada.id, *args, **kwargs)
    
    return wrapper