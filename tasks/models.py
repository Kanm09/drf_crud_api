from django.db import models

# Create your models here.
class Tasks(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)