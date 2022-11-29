from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    materia = models.IntegerField()
    autor = models.CharField(max_length=50)
    edicion = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'

    def __str__(self) :
        return self.titulo