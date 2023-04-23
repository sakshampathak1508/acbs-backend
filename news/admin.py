from django.contrib import admin
from . models import News,NewsWriter
# Register your models here.
@admin.register(News)
class NewsPostAdmin(admin.ModelAdmin):
    exclude = ('slug','year',)

admin.site.register(NewsWriter)