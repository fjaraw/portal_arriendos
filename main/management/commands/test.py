from django.core.management.base import BaseCommand
from main.services import *
# se ejecuta: python manage.py test
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #prueba de funciones desde services.py
        print('Testeo de programa')
        #crear_user(123456789, 'John', 'Doe', 'johndoe@xyz.com', '1234', 'Hill St. 1010', '+56911223344')
        #crear_user(12345678-0, 'Jane', 'Doe', 'janedoe@xyz.com', '1234', '1234', 'Hill St. 1010', '+56911223344')
        #eliminar_user('123456780')
        editar_user(123456789, 'John', 'Doe', 'johndoe@hotmail.com', '12345', 'Hill St. 1010', '+56911223344')
        print('Operación realizada.')