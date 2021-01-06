from django.shortcuts import render
from Music.forms.songmaker_form import SongMakerForm
from Music.models.songmaker import SongMaker
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def index(request, songmaker_id):
    songmaker = SongMaker.objects.get(pk=songmaker_id)
    if request.method == 'POST':
        songmaker.delete()
        return HttpResponseRedirect(reverse('songmaker_index'))
    context = {
        'songmaker': songmaker
    }
    return render(request, 'songmaker_delete/index.html', context=context)