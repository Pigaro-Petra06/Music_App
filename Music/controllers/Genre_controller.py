from django.shotcuts import render
from Music.models import Genre

def list_genre(request):
    # get all authors and add to context dictionary
    genre = Genre.objects.all()
    context = {
        'genre': genre,
    }
    # process the template and pass the context
    return render(request, 'genre.html', context=context)
