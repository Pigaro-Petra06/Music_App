from django.shortcuts import render
from Music.models.genre import Genre
from Music.models.song import Song
from Music.models.songmaker import SongMaker
from Music.models.year import Year
from Music.models.album import Album
from Music.models.region import Region

def index(request):
    # get all info here including authors, books, and genres
    num_songs = Song.objects.all().count()
    num_songmaker = SongMaker.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_year = Year.objects.all().count()
    num_album = Album.objects.all().count()
    num_region = Region.objects.all().count()

    context = {
        'num_songs': num_songs,
        'num_songmaker': num_songmaker,
        'num_genre': num_genre,
        'num_year' : num_year,
        'num_album' : num_album,
        'num_region' : num_region,
    }
    return render(request, 'index.html', context=context)