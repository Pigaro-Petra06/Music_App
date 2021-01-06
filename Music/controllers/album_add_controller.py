from django.shortcuts import render
from Music.forms.album_form import AlbumForm
from Music.models.album import Album
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def index(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('album_index'))
    else:
        form = AlbumForm()
    context = {
        'form': form
    }
    return render(request, 'album_add/index.html', context=context)