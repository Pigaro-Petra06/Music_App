from django.contrib import admin
from Music.models import genre
from Music.models import song
from Music.models import songmaker
from Music.models import year
from Music.models import album
from Music.models import region

# Register your models here.
admin.site.register(genre.Genre)
admin.site.register(song.Song)
admin.site.register(songmaker.SongMaker)
admin.site.register(year.Year)
admin.site.register(album.Album)
admin.site.register(region.Region)