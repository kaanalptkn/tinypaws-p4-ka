from django.urls import path
from . import views

urlpatterns = [
    path('', views.help_us, name='help_us'),
    path('help_us', views.adoption, name='adoption'),
]