from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):    
    horario = models.ForeignKey('Horario', on_delete=models.SET_NULL, blank=True, null=True)

class Horario(models.Model):
    horaInicio = models.IntegerField()
    horaFim = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return str(self.horaInicio) + ":00 - " + str(self.horaFim) + ":00"