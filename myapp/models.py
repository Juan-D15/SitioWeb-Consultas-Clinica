from django.db import models


# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    nacimiento = models.DateField()
    dpi = models.CharField(max_length=20, unique=True, null=False, blank=False)
    direccion = models.TextField()
    telefono = models.CharField(
        max_length=15, unique=True, null=False, blank=False
    )  # Ajusta el max_length según sea necesario.
    razon_visita = models.TextField(null=False, blank=True)
    receta_medica = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre


class Medicos(models.Model):
    nombre_medico = models.CharField(max_length=100, null=False, blank=False)
    telefono_medico = models.CharField(
        max_length=15, unique=True, null=False, blank=False
    )
    numero_colegiado = models.CharField(
        max_length=20, unique=True, null=False, blank=False
    )
    especialidad = models.CharField(max_length=50, null=False, blank=False)
    diagnostico = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre_medico
