from django.forms import ModelForm
from django.core.exceptions import ValidationError
from Music.models.album import Album 

class AlbumForm(ModelForm):
    class Meta:
        model = Album  # model to use in form
        # list of fields to be displayed
        fields = ['album', 'year']