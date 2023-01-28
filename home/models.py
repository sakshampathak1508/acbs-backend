from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField
# Create your models here.

class Annoucement(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='announcements/images',blank=True,null=True)
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):           
        return self.title


class Sponser(models.Model):    
    name = models.CharField(max_length=200,default="")    
    image = models.ImageField(upload_to='sponser/image',blank=True,null=True)    
    url = models.URLField(max_length=200,blank=True,null=True)        

    def __str__(self):           
        return self.name


class AboutUs(models.Model):
    content = QuillField(blank=True)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"
    
    def __str__(self):           
        return "About Us"
