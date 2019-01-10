from django.contrib import admin
from .models import Artwork
from django.urls import path
from django.template.response import TemplateResponse

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'active', 'timesPlayed', 'created_datetime', 'edited_datetime')
    list_editable = ('active',)
    list_filter = ('active','timesPlayed')
    list_per_page = 20
    search_fields = ('name', 'author', 'url')

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('rmngp/', self.admin_site.admin_view(self.rmngp)),
        ]
        return my_urls + urls

    def rmngp(self, request):
        context = dict(
           self.admin_site.each_context(request),
           # key=value,
        )
        return TemplateResponse(request, "admin_rmngp.html", context)
