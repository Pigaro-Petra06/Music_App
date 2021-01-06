from django.db import models
from Music.models.songmaker import SongMaker
from Music.models.genre import Genre

class Song(models.Model):
    song = models.CharField(max_length=200)
    singer = models.ForeignKey('SongMaker', on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, null=True)
    #isbn = models.CharField('ISBN', max_length=13, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.song}'