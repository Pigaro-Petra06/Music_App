from django.shortcuts import render
from Music.forms.album_form import AlbumForm
from Music.models.album import Album
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
@login_required

def index(request, album_id):
    if request.method == 'POST':
        album = Album.objects.get(pk=album_id)
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('album_index'))
    else:
        album = Album.objects.get(pk=album_id)
        fields = model_to_dict(album)
        form = AlbumForm(initial=fields, instance=album)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'album_add/index.html', context=context)