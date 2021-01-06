from django.forms import ModelForm
from django.core.exceptions import ValidationError
from Music.models.song import Song 

class SongForm(ModelForm):
    class Meta:
        model = Song  # model to use in form
        # list of fields to be displayed
        fields = ['song', 'description', 'singer', 'genre', 'region']