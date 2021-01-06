from django.db import models
from Music.models.year import Year

class Album(models.Model):
    album = models.CharField(max_length=200)
    year = models.ForeignKey('Year', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.album} {self.year}'