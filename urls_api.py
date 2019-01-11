from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from museum.models import Artwork

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artwork
        fields = ('name', 'author', 'url')
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('artworks', ArtworkViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]
