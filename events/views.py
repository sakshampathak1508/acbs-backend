from django.shortcuts import render

# Create your views here.
from . models import Event
from . serializers import (
    EventCardSerializer, EventSerializer
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        obj = Event.objects.filter(year=y).order_by('-start_date')
        ser = EventCardSerializer(obj,many=True)
        return Response(ser.data)

class EventView(APIView):
    def get(self, request, *args, **kwargs):
        nid = request.GET.get('id','')
        obj = Event.objects.filter(id=nid).first()
        ser = EventSerializer(obj)
        return Response(ser.data)
