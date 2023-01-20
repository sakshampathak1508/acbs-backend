from rest_framework import serializers
from django.utils import timezone
from .models import (
    News   
)

class CardNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','slug','image')

class NewsSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, instance):
        return str(instance.content.html)

    class Meta:
        model = News
        fields = ["id","title","category","acbs_category","image","timestamp","year","views","slug","content",]

class NewsCatogorySerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','timestamp','slug','image','acbs_category')