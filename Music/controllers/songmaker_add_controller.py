from django.shortcuts import render
from Music.forms.songmaker_form import SongMakerForm
from Music.models.songmaker import SongMaker
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def index(request):
    if request.method == 'POST':
        form = SongMakerForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('songmaker_index'))
    else:
        form = SongMakerForm()

    context = {
        'form': form
    }
    return render(request, 'songmaker_add/index.html', context=context)