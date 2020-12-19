from django.contrib import admin
from .models import Artwork
from .models import Origin
from .models import Country
import os
from django.urls import path
from django.template.response import TemplateResponse


admin.site.register(Country)

admin.site.register(Origin)

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_datetime', 'edited_datetime')
    list_display = ('name', 'author', 'active', 'date_display', 'timesPlayed', 'created_datetime', 'edited_datetime')
    list_editable = ('active',)
    list_filter = ('active','timesPlayed')
    list_per_page = 20
    search_fields = ('name', 'author', 'url_online', 'url_local')

    fieldsets = (
        ('Mandatory settings', {
            'fields': ('name', 'url_online', 'url_local')
        }),
        ('Optional settings', {
            'fields': ('author', 'author_country', 'date_display', 'active')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('timesPlayed', 'origin', 'origin_artwork_id', 'created_datetime', 'edited_datetime'),
        }),
    )

    change_form_template = 'museum/admin/change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('rmngp/', self.admin_site.admin_view(self.add_from_rmngp)),
            path('metmuseum/', self.admin_site.admin_view(self.add_from_metmuseum)),
            path('rijks/', self.admin_site.admin_view(self.add_from_rijks)),
        ]
        return my_urls + urls

    def add_from_rmngp(self, request):
        context = dict(
           self.admin_site.each_context(request),
           RMNGP_API_KEY=os.getenv('RMNGP_API_KEY'),
        )
        return TemplateResponse(request, 'museum/admin/add_from_rmngp.html', context)

    def add_from_metmuseum(self, request):
        context = dict(self.admin_site.each_context(request),)
        return TemplateResponse(request, 'museum/admin/add_from_metmuseum.html', context)

    def add_from_rijks(self, request):
        context = dict(
            self.admin_site.each_context(request),
            RIJKS_API_KEY=os.getenv('RIJKS_API_KEY'),
        )
        return TemplateResponse(request, 'museum/admin/add_from_rijks.html', context)
