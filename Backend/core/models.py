from django.db import models

class NewsEvent(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/')
    caption = models.CharField(max_length=255, blank=True)

