from django.shortcuts import render

# Create your views here.
from . models import News
from . serializers import NewsSerializer,CardNewsSerializer,NewsCatogorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import pagination,generics

class CustomPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    page_query_param = 'p'

class AllNewsApiView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-timestamp')
    serializer_class = CardNewsSerializer
    pagination_class = CustomPagination

class YearNewsView(APIView):
    def get(self, request, *args, **kwargs):
        y = request.GET.get('year','')
        obj = News.objects.filter(year=y).order_by('-timestamp')
        ser = CardNewsSerializer(obj,many=True)
        return Response(ser.data)

class NewsView(APIView):
    def get(self, request, *args, **kwargs):
        nid = request.GET.get('id','')
        obj = News.objects.filter(id=nid).first()
        if obj:
            obj.views += 1
            obj.save()
        ser = NewsSerializer(obj)
        return Response(ser.data)

class LatestNewsView(APIView):
    def get(self, request, *args, **kwargs):
        obj = News.objects.filter(category=1).order_by('-timestamp')[:9]
        ser = CardNewsSerializer(obj,many=True)        
        return Response(ser.data, status = status.HTTP_200_OK)
