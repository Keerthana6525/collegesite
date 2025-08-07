from django.urls import path
from .views import NewsEventList, AnnouncementList, CarouselImageList

urlpatterns = [
    path('news', NewsEventList.as_view(),name='news-list'),
    path('announcements/', AnnouncementList.as_view(),name='announcement-list'),
    path('carousel-images/', CarouselImageList.as_view(),name='carousel-list'),
]