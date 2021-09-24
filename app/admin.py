from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Person, Job, PriceDay, Service

admin.site.register(Person)
admin.site.register(Job)
admin.site.register(PriceDay)
admin.site.register(Service)