from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Artwork
import random

class Index(View):
    def get(self, request):
        # return render(request, 'museum/index.html', {
        return render(request, 'museum/index.oldBrowser.html', {
            'numberOfArtworks': Artwork.objects.filter(active=1).count()
        })

class Next(View):
    def get(self, request):
        # get count of smallest "timesPlayed"
        smallestTimesPlayed = Artwork.objects.filter(active=1).order_by('timesPlayed').first().timesPlayed
        countOfSmallest = Artwork.objects.filter(timesPlayed=smallestTimesPlayed, active=1).count()
        # get random artwork
        offset = random.randint(0, countOfSmallest-1)
        artwork = Artwork.objects.filter(timesPlayed=smallestTimesPlayed, active=1)[offset:offset+1].get()
        # increment timesPlayed
        artwork.timesPlayed += 1
        artwork.save()
        # return as json
        return JsonResponse(artwork.as_dict())

class Reset(View):
    def get(self, request):
        Artwork.objects.all().update(timesPlayed=0)
        return HttpResponse('OK')
