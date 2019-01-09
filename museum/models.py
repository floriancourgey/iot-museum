from django.db import models
from datetime import datetime

class Artwork(models.Model):
    created_datetime = models.DateTimeField(default=datetime.now)
    edited_datetime = models.DateTimeField(default=datetime.now)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    timesPlayed = models.IntegerField(default=0)
    origin = models.CharField(max_length=255)
    def as_dict(self):
        d = self.__dict__
        del d['_state']
        return d
    def __str__(self):
        return '"'+self.name+'" by '+str(self.author)+' ( '+self.url+' )'
