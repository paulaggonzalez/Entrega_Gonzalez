from django.db import models

# Create your models here.

class NoticiaBlog(models.Model):
    TipoNoticia = (
    ('mascotas','Mascotas'),
    ('viajes','Viajes'),
    ('tecnologia','Tecnologia'),
    ('entrenamiento','Entrenamiento'),
    )
    
    autor = models.CharField(max_length=300)
    categoriaN = models.CharField(max_length=20, choices=TipoNoticia, default='')
    encabezado = models.CharField(max_length=300)
    descripcion = models.TextField(null=False, blank=False)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    imagenNoticias = models.ImageField(null=False, blank=False, upload_to="imagenes/")
