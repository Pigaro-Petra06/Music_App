from django.shortcuts import render
from Music.models.song import Song

def index(request):
    # get all authors and add to context dictionary
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    # process the template and pass the context
    return render(request, 'song/index.html', context=context)