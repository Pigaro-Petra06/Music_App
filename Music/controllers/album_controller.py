from django.shortcuts import render
from Music.models.album import Album

def index(request):
    # get all authors and add to context dictionary
    album = Album.objects.all()
    context = {
        'album': album,
    }
    # process the template and pass the context
    return render(request, 'album/index.html', context=context)