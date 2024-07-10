from main.models import Comuna, Inmueble, UserProfile
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, bagnos, direccion, tipo_de_inmueble, precio, precio_uf, comuna, rut_propietario):
    comuna = Comuna.objects.get(nombre=comuna)
    propietario = User.objects.get(username=rut_propietario)
    inmueble = Inmueble.objects.create(
        nombre = nombre,
        descripcion = descripcion,
        m2_construidos = m2_construidos,
        m2_totales = m2_totales,
        estacionamientos = estacionamientos,
        habitaciones = habitaciones,
        bagnos = bagnos,
        direccion = direccion,
        tipo_de_inmueble = tipo_de_inmueble,
        precio = precio,
        precio_uf = precio_uf,
        comuna = comuna,
        propietario = propietario
    )
    inmueble.save()
def editar_inmueble(*args):
    pass
def eliminar_inmueble(inmueble_id):
    inmueble = Inmueble.objects.get(id = inmueble_id)
    inmueble.delete()
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
def editar_user(username, first_name, last_name, email, password, direccion, telefono=None) -> list[bool, str]:
    #Buscamos el 'user' correspondiente
    user = User.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password(password) #Mantiene encriptación de contraseña
    user.save()
    #buscamos el 'user_profile'
    user_profile = UserProfile.objects.get(user=user)
    user_profile.direccion = direccion
    user_profile.telefono = telefono
    user_profile.save()
def eliminar_user(rut):
    usuario = User.objects.get(username=rut)
    usuario.delete()