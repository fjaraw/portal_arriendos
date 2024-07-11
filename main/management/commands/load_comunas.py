from django.core.management.base import BaseCommand
import csv
from main.models import Comuna
# se ejecuta: python manage.py load_comunas
# se usa solo cuando recién creamos nuestra base de datos
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/comunas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        #avanza una línea para omitir encabezados de la tabla
        next(reader)
        for fila in reader:
            Comuna.objects.create(nombre=fila[0],cod=fila[1],region_id=fila[3])
            #print(fila[0])