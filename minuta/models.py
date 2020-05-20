from django.db import models
from platillo.models import Platillo

class Minuta(models.Model):
    nombre = models.CharField(max_length=100)
    platillo = models.ManyToManyField(Platillo, related_name='platillo')


    def __str__(self):
        return self.nombre
