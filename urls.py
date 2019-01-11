from django.contrib import admin
from django.urls import include, path
from past.builtins import execfile

urlpatterns = [
    path('', include('museum.urls')),
    path('admin/', admin.site.urls),
]

execfile('urls_api.py')
