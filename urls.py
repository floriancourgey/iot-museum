from django.contrib import admin
from django.urls import include, path

admin.site.login_template = 'admin_login.html'

urlpatterns = [
    path('', include('museum.urls')),
    path('admin/', admin.site.urls),
]
