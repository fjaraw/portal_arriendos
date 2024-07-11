from django.core.management.base import BaseCommand
import csv
from main.models import Region
# se ejecuta: python manage.py load_regiones
# se usa solo cuando recién creamos nuestra base de datos
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/comunas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        #avanza una línea para omitir encabezados de la tabla
        next(reader)
        #lista para almacenar nombre de regiones para evitar repeticiones
        nombres_regiones = []
        for fila in reader:
            if fila[2] not in nombres_regiones:
                #si el nombre de la región no está guardada, se agrega a la base de datos
                Region.objects.create(nombre=fila[2],cod=fila[3])
                #registramos el nombre en la lista para no repetir nombres
                nombres_regiones.append(fila[2])
                #print(fila[2])