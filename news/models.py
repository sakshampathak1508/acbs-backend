from django.db import models
import datetime
from django.utils import timezone
from django.http import HttpRequest
from django_quill.fields import QuillField
from django.contrib.auth.models import User

# Create your models here.
NEWS_CATEGORY = (
    (1,'LATEST'),
    (2, 'FEATURED'),
)

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

class NewsWriter(models.Model):
    name = models.CharField(max_length=256,blank=True,null=True)
    title = models.CharField(max_length=256,blank=True,null=True)
    image = models.ImageField(upload_to='news/writer',blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200,default="")
    category = models.PositiveIntegerField(choices=NEWS_CATEGORY)
    acbs_category = models.PositiveIntegerField(choices=ACBS_CATEGORY,blank=True,null=True)
    image = models.ImageField(upload_to='news/images',blank=True,null=True)
    timestamp  = models.DateTimeField(default = timezone.now)
    year = models.CharField(max_length=4)
    views = models.IntegerField(default=0)
    content = QuillField(blank=True)
    slug = models.CharField(max_length=256,blank=True,null=True)
    writer = models.ForeignKey(NewsWriter,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        value = self.title.lower()
        self.slug = value.replace(' ','-')
        y = self.timestamp.year
        self.year = y
        super().save(*args,**kwargs)