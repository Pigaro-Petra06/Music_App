from django.shortcuts import render
from Music.forms.album_form import AlbumForm
from Music.models.album import Album
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def index(request, album_id):
    album = Album.objects.get(pk=album_id)
    if request.method == 'POST':
        album.delete()
        return HttpResponseRedirect(reverse('album_index'))
    context = {
        'album': album
    }
    return render(request, 'album_delete/index.html', context=context)