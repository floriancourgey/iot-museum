from django.db import models
from datetime import datetime

class Artwork(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)
    url_online = models.URLField(max_length=255, default='', blank=True)
    url_local = models.ImageField(upload_to='artworks', default='', blank=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_display = models.CharField(max_length=255, default='', blank=True) # text date (15th century, renaissance, 1789..)
    timesPlayed = models.IntegerField(default=0) # number of times this artwork has been played
    origin = models.CharField(max_length=255) # origin system (crawler site, backoffice..)
    origin_id = models.CharField(max_length=255, default='', blank=True) # id in the origin system
    active = models.BooleanField(default=True)

    def as_dict(self):
        d = self.__dict__
        d['url_local'] = self.url_local.name
        del d['_state']
        return d

    def __str__(self):
        return '"'+self.name+'" by '+str(self.author)

    def existing(self):
        '''search by url_online|name|origin+origin_id'''
        a = Artwork.objects.filter(url_online=self.url_online).first()
        if a:
            return a
        a = Artwork.objects.filter(name=self.name).first()
        if a:
            return a
        print(self)
        print(self.__dict__)
        print(self.origin)
        print(self.origin_id)
        if self.origin and self.origin_id:
            a = Artwork.objects.filter(origin=self.origin, origin_id=self.origin_id).first()
            if a:
                return a
        return None
