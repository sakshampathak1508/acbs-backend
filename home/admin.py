from django.contrib import admin

from .models import Annoucement, Sponser, AboutUs

# Register your models here.
admin.site.register(Annoucement)
admin.site.register(Sponser)
admin.site.register(AboutUs)