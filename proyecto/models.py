from django.db import models

# Create your models here.

#===============================================================================
# Se ingresa la informacion a la base de datos
#===============================================================================

class ingreso(models.Model):
    ciudad = models.CharField(max_length=50)
    nodo = []
    coordenadaX= models.IntegerField()
    coordenadaY= models.IntegerField()

    