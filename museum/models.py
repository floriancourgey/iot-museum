from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Country(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    alpha2 = models.CharField(max_length=2)
    alpha3 = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class Origin(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    id = models.CharField(primary_key=True, max_length=255)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)
    url_online = models.URLField(max_length=255, default='', blank=True)
    url_local = models.ImageField(upload_to='artworks', default='', blank=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='', blank=True)
    author_country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True)
    date_display = models.CharField(max_length=255, default='', blank=True) # text date (15th century, renaissance, 1789..)
    timesPlayed = models.IntegerField(default=0) # number of times this artwork has been played
    active = models.BooleanField(default=True)
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT)
    origin_artwork_id = models.CharField(max_length=255, default='', blank=True) # id in the origin system

    def as_dict(self):
        d = self.__dict__
        d['url_local'] = self.url_local.name
        # add country alpha2
        d["author_country_alpha2"] = self.author_country.alpha2 if self.author_country else None
        del d['_state']
        return d

    def __str__(self):
        return '"'+self.name+'" by '+str(self.author)
