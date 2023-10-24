from django.db import models
from django.utils import timezone
# Create your models here.

class Biblioteca(models.Model):
    fecha_creacion = models.DateField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=9, unique=True)
    
class Libro(models.Model):
    IDIOMAS = [
        ("ES", "Español"),
        ("EN", "Inglés"),
        ("FR", "Francés"),
        ("IT", "Italiano"),
    ]

    nombre = models.CharField(max_length=200)
    idioma = models.CharField(
        max_length=2,
        choices=IDIOMAS,
        default="ES",
    )
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    fecha_publicacion = models.DateField()   
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    telefono = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=200, unique=True)
    puntos = models.FloatField(default=5.0, db_column="puntos_biblioteca")
    
    
class DatosCliente(models.Model):
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField(null=True, blank=True)
    altura = models.FloatField(db_column="altura_cliente")
    peso = models.FloatField(db_column="peso_cliente")  
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    
class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now)
    
    
