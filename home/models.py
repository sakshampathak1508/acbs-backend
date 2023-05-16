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
    name = models.CharField(max_length=100,blank=True,null=True)
    president = models.CharField(max_length=100,blank=True,null=True)
    flag = models.ImageField(upload_to='countries',blank=True,null=True)
    site= models.URLField(blank=True, null=True)
    email = models.URLField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True,null=True)

    class Meta:
        verbose_name = "Member Country"
        verbose_name_plural = "Member Countries"
    
    def __str__(self) -> str:
        return self.name
    
class Executive(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='executives',blank=True,null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    email = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Download(models.Model):
    name = models.CharField(max_length=200,default="")
    file = models.FileField(upload_to='home/files',blank=True,null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Download Files"
        verbose_name_plural = "Download Files"

    def __str__(self):
        return self.name

class Rule(models.Model):
    content = QuillField(blank=True)

    class Meta:
        verbose_name = "Rule"
        verbose_name_plural = "Rules"
    
    def __str__(self):           
        return "Rules"

class PastChampion(models.Model):
    name = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to="rule/images",blank=True,null=True)
    caption = models.CharField(max_length=100,default="",blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    slug = models.CharField(max_length=256,blank=True,null=True)

    def save(self,*args,**kwargs):
        value = self.name.lower()
        self.slug = value.replace(' ','-')
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Contact(models.Model):
    address = models.TextField(blank=True)
    bank_details = models.TextField(blank=True)
    name1 = models.CharField(max_length=200,blank=True,null=True)
    email1 = models.EmailField(max_length=200,blank=True,null=True)
    name2 = models.CharField(max_length=200,blank=True,null=True)
    email2 = models.EmailField(max_length=200,blank=True,null=True)
    name3 = models.CharField(max_length=200,blank=True,null=True)
    email3 = models.EmailField(max_length=200,blank=True,null=True)
    name4 = models.CharField(max_length=200,blank=True,null=True)
    email4 = models.EmailField(max_length=200,blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return 'contact us details'

