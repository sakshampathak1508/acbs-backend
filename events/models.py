from django.db import models
import datetime
from django.utils import timezone
from django.http import HttpRequest
from django_quill.fields import QuillField

ACBS_CATEGORY = (
    (1,'Snooker'),
    (2,'Billiards'),
    (3,'10Red'),
    (4,'6Red'),
    (5,'Team'),
    (6,'Juniors'),
    (7,'8Ball Pool'),
    (8,'9Ball Pool'),
    (9,'10Ball Pool'),
    (10,'World Cup'),
)

class Event(models.Model):
    
    name = models.CharField(max_length=265,default="")
    acbs_category = models.PositiveIntegerField(choices=ACBS_CATEGORY,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    venue = models.CharField(max_length=200,blank=True,null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    results = models.URLField(blank=True,null=True)
    photographs = models.URLField(blank=True,null=True)
    video = models.URLField(blank=True,null=True)
    live = models.URLField(blank=True,null=True)
    content1 = QuillField(blank=True)
    content2 = QuillField(blank=True)
    slug = models.CharField(max_length=256,blank=True,null=True)
    year = models.CharField(max_length=4,blank=True,null=True)

    def save(self,*args,**kwargs):
        value = self.name.lower()
        self.slug = value.replace(' ','-')
        y = self.start_date.year
        self.year = y
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name