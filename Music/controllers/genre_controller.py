from django.shortcuts import render
from Music.models.genre import Genre

def index(request):
    # get all authors and add to context dictionary
    genre = Genre.objects.all()
    context = {
        'genre': genre,
    }
    # process the template and pass the context
    return render(request, 'genre/index.html', context=context)