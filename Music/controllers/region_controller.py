from django.shortcuts import render
from Music.models.region import Region

def index(request):
    # get all authors and add to context dictionary
    region = Region.objects.all()
    context = {
        'region': region,
    }
    # process the template and pass the context
    return render(request, 'region/index.html', context=context)