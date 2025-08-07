from django.shortcuts import render
from rest_framework import generics
from .models import NewsEvent, Announcement, CarouselImage
from .serializers import NewsEventSerializer, AnnouncementSerializer, CarouselImageSerializer

class NewsEventList(generics.ListAPIView):
    queryset = NewsEvent.objects.all()
    serializer_class = NewsEventSerializer

class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.objects.all().order_by('-date')
    serializer_class = AnnouncementSerializer

class CarouselImageList(generics.ListAPIView):
    queryset = CarouselImage.objects.all()
    serializer_class = CarouselImageSerializer

