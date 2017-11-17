from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    link = models.CharField(max_length=100, default='www.google.com')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class usuario(models.Model):
    usuario = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    contra = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)