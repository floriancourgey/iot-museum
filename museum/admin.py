from django.contrib import admin
from .models import Artwork

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'active', 'created_datetime', 'edited_datetime')
    list_editable = ('active',)
    list_filter = ('active',)
    list_per_page = 20
    search_fields = ('name', 'author', 'url')
