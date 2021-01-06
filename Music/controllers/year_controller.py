from django.shortcuts import render
from Music.models.year import Year

def index(request):
    # get all authors and add to context dictionary
    year = Year.objects.all()
    context = {
        'year': year,
    }
    # process the template and pass the context
    return render(request, 'year/index.html', context=context)