from django.core.management.base import BaseCommand
from main.services import *
# se ejecuta: python manage.py test
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #prueba de funciones desde services.py
        print('Testeo de programa')
        #crear_user(123456789, 'John', 'Doe', 'johndoe@xyz.com', '1234', '1234', 'Hill St. 1010', '+56911223344')
        #crear_user(123456780, 'Jane', 'Doe', 'janedoe@xyz.com', '1234', '1234', 'Hill St. 1010', '+56911223344')
        #eliminar_user('123456780')
        #editar_user(123456789, 'John', 'Doe', 'johndoe@hotmail.com', '12345', 'Hill St. 1010', '+56911223344')
        #crear_inmueble('Casa Tradicional', 'Casa de dos pisos en sector regional', 120, 2000, 1, 4, 2, 'Eliodoro Yañez 1642', 'casa', 11000000, 14101, '123456789')
        #eliminar_inmueble(1)
        #editar_inmueble(2, 'Casa Tradicional', 'Casa de dos pisos en sector regional', 120, 2000, 1, 4, 1, 'Eliodoro Yañez 1642', 'casa', 210000000, 14101, '123456789')
        print('Operación realizada.')