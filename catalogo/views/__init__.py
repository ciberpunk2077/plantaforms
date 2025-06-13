# catalogo/views/__init__.py
from .planta import PlantaCreateView, PlantaListView, PlantaDetailView
from .muestra import MuestraCreateView, MuestraListView  # etc

__all__ = [
    'PlantaCreateView',
    'PlantaListView',
    'PlantaDetailView',
    'MuestraCreateView',
    # ...
]