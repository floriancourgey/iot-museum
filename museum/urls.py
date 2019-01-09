from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('next', views.Next.as_view(), name='next'),
    path('reset-times-played', views.Reset.as_view(), name='reset'),
]
