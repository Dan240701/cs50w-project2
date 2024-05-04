from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categoria(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=200)
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"

class Oferta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="usuario_oferta")
    oferta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.oferta}"

class Lista(models.Model):
    titulo = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=200)
    precio  = models.ForeignKey(Oferta, on_delete=models.CASCADE, null=True, blank=True, related_name="oferta_lista")
    image_url = models.CharField(max_length=200)
    es_activo = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="vendedor")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True, related_name="categoria")
  

    def __str__(self):
        return f"{self.titulo}"
    
    
class Comentario(models.Model):
    comentario = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="usuario")
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, null=True, blank=True, related_name="listado")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comentario} de {self.user}"
    

  
