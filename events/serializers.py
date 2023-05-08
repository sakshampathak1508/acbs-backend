from rest_framework import serializers
from django.utils import timezone
from .models import (
    Event
)

class EventCardSerializer(serializers.ModelSerializer):
    event_banner = serializers.ReadOnlyField(source='event_banner.url')
    class Meta:
        model = Event
        fields = ('id','name','slug','location','start_date','end_date',"event_banner","acbs_category")

class EventFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','name','slug','location','start_date','end_date',"acbs_category")

class EventFeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','name','slug','event_banner','groups','knockouts','results','live','photographs','video')

class EventSerializer(serializers.ModelSerializer):
    content1 = serializers.SerializerMethodField()
    content2 = serializers.SerializerMethodField()

    def get_content1(self, instance):
        return str(instance.content1.html)

    def get_content2(self, instance):
        return str(instance.content2.html)

    class Meta:
        model = Event
        fields = ["id","name","slug","acbs_category","event_banner","location","venue","start_date","end_date","groups","knockouts","results","live","photographs","video","year","content1","content2",]