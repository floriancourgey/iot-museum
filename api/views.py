from rest_framework import serializers, viewsets
from django.shortcuts import render
from django.contrib.auth.models import User
from museum.models import Artwork

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
        fields = ('id', 'name', 'author', 'url',
            'origin', 'active',
            'created_datetime')
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
