from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('artworks', views.ArtworkViewSet)
# router.register('gameUsers', views.GameUserViewSet)
router.register('games', views.GameViewSet)
# router.register('gameEvents', views.GameEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
