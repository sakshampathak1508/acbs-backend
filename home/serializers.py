from rest_framework import serializers
from .models import Annoucement, Sponser, AboutUs

class SponsersSerializers(serializers.Serializer):
    class Meta:
        model = Sponser
        fields = '__all__'

class AnnouncementSerializer(serializers.Serializer):
    class Meta:
        model = Annoucement
        fields = '__all__'

class AboutUsSerializer(serializers.Serializer):
    content = serializers.SerializerMethodField()

    def get_content(self, instance):
        return str(instance.content.html)
    
    class Meta:
        model = AboutUs
        fields = ['content']