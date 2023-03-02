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


class MemberCountries(models.Model):
    name = models.CharField(max_length=100, unique=True)
    flag = models.ImageField(upload_to='countries/flags')
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    site= models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Member Country"
        verbose_name_plural = "Member Countries"
    
    def __str__(self) -> str:
        return self.name
    
class Executive(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='executives')
    title = models.CharField(max_length=200)
    origin_country = models.CharField(max_length=100, verbose_name="Country of Origin")
    def __str__(self) -> str:
        return self.name


