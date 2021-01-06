from django.shortcuts import render
from Music.forms.song_form import SongForm
from Music.models.song import Song
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def index(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('song_index'))
    else:
        form = SongForm()

    context = {
        'form': form
    }
    return render(request, 'song_add/index.html', context=context)