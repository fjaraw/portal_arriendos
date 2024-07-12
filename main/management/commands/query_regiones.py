from django.core.management.base import BaseCommand, CommandParser
from main.services import obtener_inmuebles_region
class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('-f', '--f', type=str, nargs='+',)
    def handle(self, *args, **kwargs):
        archivo = open('data/inmuebles_region.txt', 'w',encoding='utf-8')
        filtro_region = None
        if 'f' in kwargs.keys() and kwargs['f'] is not None:
            filtro_region = kwargs['f'][0]
        inmuebles = obtener_inmuebles_region(filtro_region)
        for inmueble in inmuebles:
            #import pdb; pdb.set_trace()
            linea = f'{inmueble.nombre}\t{inmueble.descripcion}\t{inmueble.comuna.region.nombre}'
            archivo.write(linea)
            archivo.write('\n')
            print(linea)
        archivo.close()