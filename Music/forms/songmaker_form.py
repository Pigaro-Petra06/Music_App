from django.forms import ModelForm
from django.core.exceptions import ValidationError
from Music.models.songmaker import SongMaker

class SongMakerForm(ModelForm):
    class Meta:
        model = SongMaker  # model to use in form
        # list of fields to be displayed
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']