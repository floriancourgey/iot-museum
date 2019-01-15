from django.db import models
from datetime import datetime

class Artwork(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=255)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    timesPlayed = models.IntegerField(default=0) # number of times this artwork has been played
    origin = models.CharField(max_length=255) # origin system (crawler site, backoffice..)
    origin_id = models.CharField(max_length=255, default=None, null=True) # id in the origin system
    active = models.BooleanField(default=True)

    def as_dict(self):
        d = self.__dict__
        del d['_state']
        return d

    def __str__(self):
        return '"'+self.name+'" by '+str(self.author)

    def existing(self):
        ''' search by url|name|origin+origin_id'''
        a = Artwork.objects.filter(url=self.url).first()
        if a:
            return a
        a = Artwork.objects.filter(name=self.name).first()
        if a:
            return a
        if self.origin and self.origin_id:
            a = Artwork.objects.filter(origin=self.origin, origin_id=self.origin_id).first()
            if a:
                return a
        return None
