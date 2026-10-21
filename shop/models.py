from django.db import models

# Create your models here.
class producto (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
class categoria(models.Model):
    producto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='categorias')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    

    def __str__(self):
        return self.nombre