from django.db import models
from django.contrib.auth.models import User

class Pi(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    numero_pi = models.FloatField(default = 0)
    def __str__(self) -> str:
        return str(self.numero_pi)

class LogPi(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    numero_pi = models.FloatField(default = 0)
    def __str__(self):
        return str(self.numero_pi)
    

class MultLogPi(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    numero_pi = models.FloatField(default = 0)
    def __str__(self) -> str:
        return str(self.numero_pi)


class Dados(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pi = models.ManyToManyField(Pi)
    logpi = models.ManyToManyField(LogPi)
    multipi = models.ManyToManyField(MultLogPi)
    resultado = models.FloatField(default= 0)
    def __str__(self) -> str:
        return f"Comunidade {str(self.resultado)}"
    