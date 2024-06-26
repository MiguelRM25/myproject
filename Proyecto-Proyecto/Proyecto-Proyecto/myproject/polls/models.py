import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    email = models.EmailField()
    telefono = models.CharField(max_length=10) 

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario
