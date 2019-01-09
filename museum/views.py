from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import Artwork
import random
from django.conf import settings

def index(request):
    return render(request, 'index.html', {
        'numberOfArtworks': Artwork.objects.count()
    })
def next(request):
    # print('API_KEY',settings.API_KEY)
    # get count of smallest "timesPlayed"
    smallestTimesPlayed = Artwork.objects.order_by('timesPlayed').all()[0].timesPlayed
    countOfSmallest = Artwork.objects.filter(timesPlayed=smallestTimesPlayed).count()
    # get random artwork
    offset = random.randint(0, countOfSmallest-1)
    artwork = Artwork.objects.filter(timesPlayed=smallestTimesPlayed)[offset:offset+1].get()
    # increment timesPlayed
    artwork.timesPlayed += 1
    artwork.save()
    # return as json
    return JsonResponse(artwork.as_dict())
