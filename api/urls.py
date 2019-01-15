from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('artworks', views.ArtworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
