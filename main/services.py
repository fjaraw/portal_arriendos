from main.models import Comuna, Inmueble, UserProfile
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def crear_inmueble(*args):
    pass
def editar_inmueble(*args):
    pass
def eliminar_inmueble(inmueble_id):
    pass
def crear_user(rut, first_name, last_name, email, password, pass_confirm, direccion, telefono=None) -> list[bool, str]:
    if password != pass_confirm:
        return False, 'Contraseñas no coinciden.'
    try:
        user = User.objects.create_user(
            username=rut,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password
        )
    except IntegrityError:
        return False, 'Rut Duplicado.'
    UserProfile.objects.create(
        direccion = direccion,
        telefono = telefono,
        user = user
        )
    return True
def editar_user(*args):
    pass
def eliminar_user(rut):
    usuario = User.objects.get(username=rut)
    usuario.delete()