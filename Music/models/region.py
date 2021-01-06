from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        app_label = 'Music'

    def __str__(self):
        return f'{self.name} '