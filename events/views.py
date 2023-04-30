from django.shortcuts import render

# Create your views here.
from . models import Event
from . serializers import (
    EventCardSerializer, EventSerializer, EventFrontSerializer
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework import pagination,generics

class CustomPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    page_query_param = 'p'

class AllEventView(generics.ListAPIView):
    queryset =Event.objects.all().order_by('-start_date')
    serializer_class = EventCardSerializer
    pagination_class = CustomPagination

class YearEventView(APIView):
    def get(self, request, *args, **kwargs):
        y = request.GET.get('year','')
        cat = request.GET.get('cat','')
        if cat:
            cat = int(cat)
        obj = []
        if y:
            if cat==1:
                obj = Event.objects.filter(Q(acbs_category='Snooker') | Q(acbs_category = 'Billiards') | Q(acbs_category = '10Red') | Q(acbs_category = '6Red') | Q(acbs_category = 'Juniors') | Q(acbs_category = 'World Cup'),year=y).order_by('-start_date')
            elif cat==2:
                obj = Event.objects.filter(Q(acbs_category = '8Ball Pool') | Q(acbs_category = '9Ball Pool') | Q(acbs_category = '10Ball Pool'),year=y).order_by('-start_date')
            else:
                obj = Event.objects.filter(year=y).order_by('-start_date')
        elif cat: 
            if cat==1:
                obj = Event.objects.filter(Q(acbs_category = 'Snooker') | Q(acbs_category = 'Billiards') | Q(acbs_category = '10Red') | Q(acbs_category = '6Red') | Q(acbs_category = 'Juniors') | Q(acbs_category = 'World Cup')).order_by('-start_date')
            elif cat==2:
                obj = Event.objects.filter(Q(acbs_category = '8Ball Pool') | Q(acbs_category = '9Ball Pool') | Q(acbs_category = '10Ball Pool')).order_by('-start_date')
        else:
            obj = []
        ser = EventCardSerializer(obj,many=True)
        return Response(ser.data)

class EventView(APIView):
    def get(self, request, *args, **kwargs):
        nid = request.GET.get('id','')
        obj = Event.objects.filter(id=nid).first()
        ser = EventSerializer(obj)
        return Response(ser.data)
    
class EventFrontView(APIView):
    def get(self, request, *args, **kwargs):
        data = {}
        sb = Event.objects.filter(Q(acbs_category = 'Snooker') | Q(acbs_category = 'Billiards') | Q(acbs_category = '10Red') | Q(acbs_category = '6Red') | Q(acbs_category = 'Juniors') | Q(acbs_category = 'World Cup'),show_on_front=True).order_by('-start_date')
        pool = Event.objects.filter(Q(acbs_category = '8Ball Pool') | Q(acbs_category = '9Ball Pool') | Q(acbs_category = '10Ball Pool'),show_on_front=True).order_by('-start_date')
        data['snooker-billiards'] = EventFrontSerializer(sb,many=True).data
        data['pool'] = EventFrontSerializer(pool,many=True).data
        return Response(data)
