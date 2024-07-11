from django.core.management.base import BaseCommand
import csv
from main.services import crear_user
# se ejecuta: python manage.py load_usuarios
# se usa solo cuando recién creamos nuestra base de datos
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/usuarios.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        #avanza una línea para omitir encabezados de la tabla
        next(reader)
        for fila in reader:
            crear_user(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],'0')
            #print(f'{fila[0]} {fila[1]} {fila[2]} {fila[3]} {fila[4]} {fila[5]} {fila[6]}')