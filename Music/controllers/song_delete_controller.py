from django.shortcuts import render
from Music.forms.song_form import SongForm
from Music.models.song import Song
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def index(request, song_id):
    song = Song.objects.get(pk=song_id)
    if request.method == 'POST':
        song.delete()
        return HttpResponseRedirect(reverse('song_index'))
    context = {
        'song': song,
    }
    return render(request, 'song_delete/index.html', context=context)