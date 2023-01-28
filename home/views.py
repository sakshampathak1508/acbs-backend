from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AboutUsSerializer, SponsersSerializers, AnnouncementSerializer
from .models import AboutUs, Annoucement, Sponser
# Create your views here.


class SponsersView(APIView):
    def get(self, request, *args, **kwargs):
        data = Sponser.objects.all()
        serializer = SponsersSerializers(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
class LatestAnnouncement(APIView):
    serializer_class = AnnouncementSerializer
    def get(self, request, *args, **kwargs):
        try:
            data = Annoucement.objects.filter(show=True).order_by('-id')[0]
            serializer = AnnouncementSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("No announcements", status=status.HTTP_404_NOT_FOUND)

class AboutUSView(APIView):
    serializer_class = AboutUsSerializer
    def get(self, request):
        data = AboutUs.objects.get()
        serializer = AboutUsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)




