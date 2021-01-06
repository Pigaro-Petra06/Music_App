from django.shortcuts import render
from Music.forms.songmaker_form import SongMakerForm
from Music.models.songmaker import SongMaker
from django.shortcuts import render
from Music.forms.songmaker_form import SongMakerForm
from Music.models.songmaker import SongMaker
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def index(request, songmaker_id):
    if request.method == 'POST':
        songmaker = SongMaker.objects.get(pk=songmaker_id)
        form = SongMakerForm(request.POST, instance=songmaker)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('songmaker_index'))
    else:
        songmaker = SongMaker.objects.get(pk=songmaker_id)
        fields = model_to_dict(songmaker)
        form = SongMakerForm(initial=fields, instance=songmaker)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'songmaker_add/index.html', context=context)