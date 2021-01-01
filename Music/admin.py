from django.contrib import admin
from Music.models import genre

# Register your models here.
admin.site.register(genre.Genre)
