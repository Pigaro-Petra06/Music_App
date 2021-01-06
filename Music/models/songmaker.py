from django.db import models

class SongMaker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        app_label = 'Music'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
