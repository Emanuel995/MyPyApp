from django import template
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/',views.PersonView.as_view(), name='persons'),
    #path('person/<int:person_id>/',views.ver_persona, name='person'),
    path('jobs/',views.JobView.as_view(),name='jobs'),
    path('job/add/',views.JobCreateView.as_view(), name='job_add'),
    path('job/<pk>/update/',views.JobUpdateView.as_view(), name='job_update'),
    path('job/<pk>/delete/',views.JobDeleteView.as_view(), name='job_delete'),
    path('job/<pk>/',views.JobDetailView.as_view(), name='job'),
    path('prices/',views.PriceListView.as_view(), name='prices'),
    path('price/<pk>/',views.PriceDetailView.as_view(), name='price'),
    path('services/',views.ServiceListView.as_view(), name='services'),
    path('service/<pk>/',views.ServiceDetailView.as_view(), name='service'),
    path('service/add',views.ServiceCreateView.as_view(), name='service_add'),
    path('service/<pk>/update',views.ServiceUpdateView.as_view(), name='service_update'),
    path('service/<pk>/delete',views.ServiceDeleteView.as_view(), name='service_delete'),
    
]