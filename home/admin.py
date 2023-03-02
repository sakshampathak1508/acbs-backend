from django.contrib import admin

from .models import Annoucement, Sponser, AboutUs, Executive, MemberCountries

# Register your models here.
admin.site.register(Annoucement)
admin.site.register(Sponser)
admin.site.register(AboutUs)
admin.site.register(Executive)
admin.site.register(MemberCountries)