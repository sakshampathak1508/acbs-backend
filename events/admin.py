from django.contrib import admin
from . models import Event
# Register your models here.
@admin.register(Event)
class NewsPostAdmin(admin.ModelAdmin):
    exclude = ('slug','year',)