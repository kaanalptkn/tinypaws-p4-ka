from django.shortcuts import render
from .models import Pets

# Create your views here.


def about(request):
    """ This is view to show about the charity """
    
    return render(request, 'about/about.html')

def pets(request):
    
    pets = Pets.objects.all()
    context = {
        'pets': pets,
    }

    return render(request, 'about/pets.html', context)

