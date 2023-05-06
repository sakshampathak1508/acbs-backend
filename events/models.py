from django.db import models
import datetime
from django.utils import timezone
from django.http import HttpRequest
from django_quill.fields import QuillField

ACBS_CATEGORY = (
    ('Snooker','Snooker'),
    ('Billiards','Billiards'),
    ('10Red','10Red'),
    ('6Red','6Red'),
    ('Team','Team'),
    ('Juniors','Juniors'),
    ('8Ball Pool','8Ball Pool'),
    ('9Ball Pool','9Ball Pool'),
    ('10Ball Pool','10Ball Pool'),
    ('World Cup','World Cup'),
)

class Event(models.Model):
    
    name = models.CharField(max_length=265,default="")
    acbs_category = models.CharField(choices=ACBS_CATEGORY,max_length=100,blank=True,null=True)
    event_banner = models.ImageField(upload_to='news/images',blank=True,null=True)
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
    is_featured = models.BooleanField(default=False)
    show_on_front = models.BooleanField(default=False)
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