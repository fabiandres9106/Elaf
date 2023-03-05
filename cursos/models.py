from django.db import models

# Create your models here.

class Preinscripcion_legislacion(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.BigIntegerField()
    acepta_terminos_y_condiciones = models.BooleanField(default=True)
    suscripcion = models.BooleanField(default=True)
    date_registro = models.DateTimeField(auto_now_add=True)