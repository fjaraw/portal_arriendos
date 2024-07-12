from django.core.management.base import BaseCommand
import csv
from main.services import crear_inmueble
# se ejecuta: python manage.py load_inmuebles
# se usa solo cuando recién creamos nuestra base de datos
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/inmuebles.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        #avanza una línea para omitir encabezados de la tabla
        next(reader)
        for fila in reader:
            crear_inmueble(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11])
            #print(f'{fila[0]} - {fila[1]} - {fila[2]} - {fila[3]} - {fila[4]} - {fila[5]} - {fila[6]} - {fila[7]} - {fila[8]} - {fila[9]} - {fila[10]} - {fila[11]}')