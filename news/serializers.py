from rest_framework import serializers
from django.utils import timezone
from .models import (
    News,NewsWriter
)

class CardNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','timestamp','slug','image','acbs_category')

class NewsSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    writer_name = serializers.ReadOnlyField(source='writer.name')
    writer_title = serializers.ReadOnlyField(source='writer.title')
    writer_image = serializers.ReadOnlyField(source='writer.image.url')


    def get_content(self, instance):
        return str(instance.content.html)

    class Meta:
        model = News
        fields = ["id","title","category","acbs_category","image","timestamp","year","views","slug","writer_name","writer_title","writer_image","content",]

class NewsCatogorySerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','timestamp','slug','image','acbs_category')