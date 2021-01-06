from django.shortcuts import render
from Music.forms.song_form import SongForm
from Music.models.song import Song
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def index(request, song_id):
    if request.method == 'POST':
        song = Song.objects.get(pk=song_id)
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('song_index'))
    else:
        song = Song.objects.get(pk=song_id)
        fields = model_to_dict(song)
        form = SongForm(initial=fields, instance=song)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'song_add/index.html', context=context)