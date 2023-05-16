from rest_framework import serializers
from .models import Annoucement, Executive, Sponser, AboutUs, MemberCountries, Download, Rule, PastChampion, Contact

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
        fields = '__all__'

class MemberCountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberCountries
        fields = '__all__'

class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download 
        fields = '__all__'

class RuleSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, instance):
        return str(instance.content.html)
    
    class Meta:
        model = Rule
        fields = ['content']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class PastChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastChampion
        fields = '__all__'

class AllChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastChampion
        fields = ('id','name','caption','image','slug')