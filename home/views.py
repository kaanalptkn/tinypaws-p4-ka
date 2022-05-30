from django.shortcuts import render

# Create your views here.


def index(request):
    """ This is view for donation on help us section"""
    
    return render(request, 'home/index.html')