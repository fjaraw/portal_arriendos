from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class UserProfile(models.Model):
    #User: username(rut), email,first_name,last_name, password
    user = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True)

class Region(models.Model):
    cod = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=255)
    
class Comuna(models.Model):
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.RESTRICT)
    def __str__(self):
        return f'{self.nombre}'

class Inmueble(models.Model):
    tipo_inmueble = (('bodega', 'Bodega'),('casa', 'Casa'), ('departamento','Departamento'), ('parcela','Parcela'))
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1500)
    m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales = models.IntegerField(validators=[MinValueValidator(1)])
    estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    bagnos = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    direccion = models.CharField(max_length=255)
    tipo_de_inmueble = models.CharField(max_length=255,choices=tipo_inmueble)
    precio = models.IntegerField(validators=[MinValueValidator(1000)], null=True)
    #llaves foráneas
    comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.RESTRICT)
    propietario = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='inmuebles')

class Solicitud(models.Model):
    estados = (('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada'))
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitud')
    arrendador = models.ForeignKey(User, related_name='solicitudes', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=estados)