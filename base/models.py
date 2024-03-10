from django.db import models

# Create your models here.


class Event(models.Model):
    lote = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(null=True, default='no-photo.svg')
    date = models.DateField()
    location = models.CharField(max_length=100)
    ticket_link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PastEvents(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(null=True, default='no-photo.svg')
    date = models.DateField()
    location = models.CharField(max_length=100)
    gallery_link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FutureEvents(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(null=True, default='no-photo.svg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

