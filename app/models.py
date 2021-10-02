from enum import auto
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.urls.base import reverse
from datetime import timedelta
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Person (models.Model):
    person_id = models.IntegerField(primary_key=True)
    person_nombre = models.CharField(max_length=100)
    person_apellido = models.CharField(max_length=100)
    person_ciut = models.IntegerField(null=True)
    person_email = models.EmailField(null=True)
    
    def __str__(self):
        return self.person_apellido+', '+self.person_nombre

    def get_absolute_url(self):
        return reverse('persons')

class Job (models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_nombre = models.CharField(max_length=100)
    job_cuit = models.IntegerField(null=True)
    job_direccion = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.job_nombre

    def get_absolute_url(self):
        return reverse('jobs')

class Service (models.Model):
    service_id = models.IntegerField(primary_key=True)
    job_id = models.ForeignKey(Job,on_delete=CASCADE)
    person_id = models.ForeignKey(Person,on_delete=CASCADE)
    service_fecha = models.DateField(null=True)
    service_hora_desde = models.TimeField(null=True)
    service_hora_hasta = models.TimeField(null=True)

    @property
    def service_hora_total (self):
        return (self.service_hora_hasta.hour - self.service_hora_desde.hour)
    
    @property
    def service_day (self):
        return self.service_fecha.isoweekday()

    @property
    def service_price_day_valor(self):
        priceday = PriceDay.objects.get(job_id = self.job_id, price_day = self.service_day)
        return priceday.price_valor
    
    @property
    def service_price_total(self):
        return self.service_price_day_valor * self.service_hora_total

class PriceDay (models.Model):
    DAYS_WEEK = [(1, 'Lunes'),(2,'Martes'),(3,'Miercoles'),(4,'Jueves'),(5,'Viernes'),(6,'Sabado'),(7,'Domingo')]
    price_id = models.IntegerField(primary_key=True)
    job_id = models.ForeignKey(Job,on_delete=CASCADE)
    price_day = models.IntegerField(choices=DAYS_WEEK)
    price_fecha_desde = models.DateField(null=True)
    price_fecha_hasta = models.DateField(null=True)
    price_valor = models.IntegerField(default=0)

