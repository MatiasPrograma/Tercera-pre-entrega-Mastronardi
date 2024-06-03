from django.db import models

class Clientes(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    
class Ropa(models.Model):
    
    Marca = models.CharField(max_length=20)
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.Marca} - {self.stock}"
    
class Vendedor(models.Model):
    
    nombre = models.CharField(max_length=20)
    idvendedor = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} - {self.idvendedor}"
    
class Consultas(models.Model):
    
    Problema = models.CharField(max_length=40)
    idproblema = models.IntegerField()
    
    def __str__(self):
        return f"{self.Problema} - {self.idproblema}"
    
    