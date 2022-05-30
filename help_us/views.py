from django.shortcuts import render

# Create your views here.


def help_us(request):
    """ This is view returning to index page"""
    
    return render(request, 'help_us/donation.html')

def adoption(request):
    return render(request, 'help_us/adoption.html')

