from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import AboutUsSerializer, ExecutiveSerializer, MemberCountriesSerializer, SponsersSerializers, AnnouncementSerializer
from .models import AboutUs, Annoucement, Executive, MemberCountries, Sponser
from news.models import News
from news.serializers import CardNewsSerializer
from events.models import Event
from events.serializers import EventCardSerializer,EventFeaturedSerializer
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


class ExecutivesView(APIView):
    serializer_class = ExecutiveSerializer
    def get(self, request):
        data = Executive.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MemberCountriesView(APIView):
    serializer_class = MemberCountriesSerializer
    def get(self, request):
        data = MemberCountries.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        output_data = {}
        query = request.GET.get('query','')
        if query:
            news_obj  = News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(year__icontains=query))
            event_obj = Event.objects.filter(Q(name__icontains=query) |  Q(location__icontains=query) |Q(venue__icontains=query) |Q(content1__icontains=query) |Q(content2__icontains=query))
            output_data['news'] =   CardNewsSerializer(news_obj,many=True).data
            output_data['events'] =   EventCardSerializer(event_obj,many=True).data
        return Response(output_data,status=status.HTTP_200_OK)

class FeaturedView(APIView):
    def get(self, request, *args, **kwargs):
        output_data = {}
        news_obj  = News.objects.filter(category=2).order_by('-timestamp')[:3]
        event_obj = Event.objects.filter(is_featured=True).order_by('-start_date')[:3]
        output_data['news'] =   CardNewsSerializer(news_obj,many=True).data
        output_data['events'] =   EventFeaturedSerializer(event_obj,many=True).data
        return Response(output_data,status=status.HTTP_200_OK)