from django.shortcuts import render

# Create your views here.


def index(request):
    """ This is view returning to index page"""
    
    return render(request, 'home/index.html')