from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from museum.models import Artwork

class ArtworkSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # check if artwork not already existing
        a = Artwork()
        a.__dict__ = validated_data
        existing = a.existing()
        if existing:
            return existing
        # otherwise, create it
        return Artwork.objects.create(**validated_data)

    class Meta:
        model = Artwork
        fields = ('id', 'name', 'author',
            'url_online', 'url_local',
            'origin', 'origin_id', 'active',
            'created_datetime')
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

    @action(detail=False, url_name='count')
    def count(self, request):
        count = self.filter_queryset(self.get_queryset()).count()
        return JsonResponse({'count': count})

    @action(detail=False, url_name='authors-count')
    def count_distinct_authors(self, request):
        count = Artwork.objects.order_by('author').values('author').distinct().count()
        return JsonResponse({'count': count})
