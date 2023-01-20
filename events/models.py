from django.db import models
import datetime
from django.utils import timezone
from django.http import HttpRequest
from django_quill.fields import QuillField
# Create your models here.

# class Event(models.Model):
#     ACBS_CATEGORY = (
#     (1,'World Snooker'),
#     (2,'World Billiards'),
#     (3,'World 6Reds'),
#     (4,'World Team'),
#     (5,'World U21'),
#     (6,'World U18'),
#     (7,'World U17'),
#     (8,'World U16'),
#     (9,'World Cup'),
# )
#     name = models.CharField(max_length=265,default="")
#     ibsf_category = models.PositiveIntegerField(choices=ACBS_CATEGORY,blank=True,null=True)
#     location = models.CharField(max_length=200,blank=True,null=True)
#     venue = models.CharField(max_length=200,blank=True,null=True)
#     start_date = models.DateField(default=timezone.now)
#     end_date = models.DateField(default=timezone.now)
#     results = models.URLField(blank=True,null=True)
#     photographs = models.URLField(blank=True,null=True)
#     video = models.URLField(blank=True,null=True)
#     live = models.URLField(blank=True,null=True)
#     content1 = models.TextField(blank=True)
#     content2 = models.TextField(blank=True)
#     show_on_front = models.BooleanField(default=False)
#     slug = models.CharField(max_length=256,blank=True,null=True)
#     year = models.CharField(max_length=4,blank=True,null=True)

#     def save(self,*args,**kwargs):
#         value = self.name.lower()
#         self.slug = value.replace(' ','-')
#         y = self.start_date.year
#         self.year = y
#         super().save(*args,**kwargs)

#     def __str__(self):
#         return self.name