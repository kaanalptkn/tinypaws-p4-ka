from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.pets, name='pets'),
    path('contact/', views.contact, name='contact'),
]