from django.db import models

class Empresa(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Beacon(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Promocion(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField()
    beacon = models.ForeignKey(Beacon, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


