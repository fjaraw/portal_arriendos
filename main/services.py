from main.models import Comuna, Inmueble, UserProfile
from django.contrib.auth.models import User

def crear_inmueble(*args):
    pass
def editar_inmueble(*args):
    pass
def eliminar_inmueble(inmueble_id):
    pass
def crear_user(rut, first_name, last_name, email, password, direccion, telefono):
    user = User.objects.create_user(
        username=rut,
        first_name = first_name,
        last_name = last_name,
        email = email,
        password = password
    )
    UserProfile.objects.create(
        direccion = direccion,
        telefono = telefono,
        user = user
        )
def editar_user(*args):
    pass
def eliminar_user(rut):
    usuario = User.objects.get(username=rut)
    usuario.delete()