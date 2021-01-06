from django.shortcuts import render
from Music.models.songmaker import SongMaker
def index(request):
    # get all authors and add to context dictionary
    songmaker = SongMaker.objects.all()
    context = {
        'songmaker': songmaker,
    }
    # process the template and pass the context
    return render(request, 'songmaker/index.html', context=context)