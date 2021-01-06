from django.urls import path
from Music.controllers import index_controller
from Music.controllers import genre_controller
from Music.controllers import songmaker_controller, songmaker_add_controller, songmaker_delete_controller, songmaker_edit_controller
from Music.controllers import year_controller
from Music.controllers import region_controller
from Music.controllers import song_controller, song_edit_controller, song_add_controller, song_delete_controller, registration_controller
from Music.controllers import album_controller, album_add_controller, album_edit_controller, album_delete_controller
urlpatterns = [
    path('', index_controller.index, name='index'),
    path('Genre/', genre_controller.index, name='genre_index'),
    path('SongMaker/', songmaker_controller.index, name='songmaker_index'),
    path('SongMaker/Add', songmaker_add_controller.index, name='songmaker_add'),
    path('SongMaker/Edit<int:songmaker_id>', songmaker_edit_controller.index, name='songmaker_edit'),
    path('SongMaker/Delete<int:songmaker_id>', songmaker_delete_controller.index, name='songmaker_delete'),
    path('Song/', song_controller.index, name='song_index'),
    path('Song/Add', song_add_controller.index, name='song_add'),
    path('Song/Edit<int:song_id>', song_edit_controller.index, name='song_edit'),
    path('Song/Delete<int:song_id>', song_delete_controller.index, name='song_delete'),
    path('Year/', year_controller.index, name='year_index'),
    path('Registration/', registration_controller.index, name='register'),
    path('Album/', album_controller.index, name='album_index'),
    path('Album/Add', album_add_controller.index, name='album_add'),
    path('Album/Edit<int:album_id>', album_edit_controller.index, name='album_edit'),
    path('Album/Delete<int:album_id>', album_delete_controller.index, name='album_delete'),
    path('Region/', region_controller.index, name='region_index'),
    
]