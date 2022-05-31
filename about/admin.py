from django.contrib import admin
from .models import Pets

# Register your models here.


class PetsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
        "weight", 
        "image_url",
        "image"
    )



admin.site.register(Pets, PetsAdmin)