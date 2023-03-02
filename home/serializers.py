from rest_framework import serializers
from .models import Annoucement, Executive, Sponser, AboutUs, MemberCountries

class SponsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sponser
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annoucement
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, instance):
        return str(instance.content.html)
    
    class Meta:
        model = AboutUs
        fields = ['content']

class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive 
        fields = ['name', 'title', 'origin_country', 'image']

class MemberCountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberCountries
        fields = ['name', 'flag', 'facebook', 'instagram', 'twitter', 'site']