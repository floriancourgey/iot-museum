from django.db import models
from datetime import datetime

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

    def existing(self):
        '''search by url_online|name|origin+origin_artwork_id'''
        a = Artwork.objects.filter(url_online=self.url_online).first()
        if a:
            return a
        a = Artwork.objects.filter(name=self.name).first()
        if a:
            return a
        print(self)
        print(self.__dict__)
        print(self.origin)
        print(self.origin_artwork_id)
        if self.origin and self.origin_artwork_id:
            a = Artwork.objects.filter(origin=self.origin, origin_artwork_id=self.origin_artwork_id).first()
            if a:
                return a
        return None

class GameUser(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=255)

class Game(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)

class GameEvent(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(GameUser, on_delete=models.PROTECT)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
