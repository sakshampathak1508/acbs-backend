from django.db import models
import datetime
from django.utils import timezone
from django.http import HttpRequest
from django_quill.fields import QuillField

# Create your models here.
NEWS_CATEGORY = (
    (1,'LATEST'),
    (2, 'FEATURED'),
)

ACBS_CATEGORY = (
    (1,'World Snooker'),
    (2,'World Billiards'),
    (3,'World 6Reds'),
    (4,'World Team'),
    (5,'World U21'),
    (6,'World U18'),
    (7,'World U17'),
    (8,'World U16'),
    (9,'World Cup'),
)

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

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        value = self.title.lower()
        self.slug = value.replace(' ','-')
        super().save(*args,**kwargs)