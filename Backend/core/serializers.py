from rest_framework import serializers
from .models import NewsEvent, Announcement, CarouselImage

class NewsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEvent
        fields = ['description', 'date']

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = '__all__'

