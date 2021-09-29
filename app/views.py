from django import template
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import context, loader
from django.template.base import Template
from django.urls import reverse
from django.views import generic
from .models import Person, Job, PriceDay, Service
from app import models


class PersonView(generic.ListView):
    models = Person
    context_object_name = 'persons'
    template_name = 'persons.html'
    queryset = Person.objects.all()

class JobView(generic.ListView):
    models = Job
    context_object_name = 'jobs'
    template_name = 'jobs.html'
    queryset = Job.objects.all()

class JobDetailView(generic.DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'job.html'

class JobCreateView(generic.CreateView):
    model = Job
    fields = ['job_id','job_nombre','job_cuit','job_direccion']
    template_name = 'job_add.html'
    #success_url = reverse('jobs')

class JobUpdateView(generic.UpdateView):
    model = Job
    fields = ['job_nombre','job_cuit','job_direccion']
    template_name = 'job_update.html'

class JobDeleteView(generic.DeleteView):
    model = Job
    fields = ['job_nombre','job_cuit','job_direccion']
    template_name = 'job_delete.html'
    success_url = '/app/jobs/'
    
class PriceListView(generic.ListView):
    model = PriceDay
    context_object_name = 'prices'
    template_name = 'prices.html'
    queryset = PriceDay.objects.all()

class PriceDetailView(generic.DetailView):
    model = PriceDay
    context_object_name = 'price'
    template_name = 'price.html'

class ServiceListView(generic.ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'services.html'
    queryset = Service.objects.all()

class ServiceDetailView(generic.DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'service.html'

class ServiceCreateView(generic.CreateView):
    model = Service
    fields = ['service_id','job_id','person_id','service_fecha','service_hora_desde','service_hora_hasta']
    template_name = 'service_add.html'
    success_url = '/app/services'

class ServiceUpdateView(generic.UpdateView):
    model = Service
    fields = ['service_id','job_id','person_id','service_fecha','service_hora_desde','service_hora_hasta']
    template_name = 'service_update.html'
    success_url = '/app/services'

class ServiceDeleteView(generic.DeleteView):
    model = Job
    fields = ['service_id','job_id','person_id','service_fecha','service_hora_desde','service_hora_hasta']
    template_name = 'service_delete.html'
    success_url = '/app/jobs/'


def index(request):
    template = loader.get_template('index.html')
    context = { }
    return HttpResponse(template.render(context,request))

def ver_trabajo(request, job_id):
    try:
        j = Job.objects.get(job_id = job_id )
        template = loader.get_template('jobs.html')
        context = { 'job' : j }
    except Job.DoesNotExist:
        raise Http404("No Existe Job")
    
    return HttpResponse(template.render(context,request))

