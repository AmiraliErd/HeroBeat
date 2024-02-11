from django.urls import path
from . import views

app_name = 'Tracks'
urlpatterns = [
    path('songs/', views.tracks_list, name='songs'),
    path('albums/', views.albums_list, name='albums'),
    path('albums/detail/<slug:slug>', views.album_details, name='album_detail'),
    path('albums/detail/<slug:slug>/320', views.album_320, name='album_320'),
    path('albums/detail/<slug:slug>/128', views.album_128, name='album_128'),
    path('songs/detail/<slug:slug>', views.track_details, name='track_detail'),
    path('artist/detail/<slug:slug>', views.artist_details, name='artist_detail'),
    path('search/', views.search, name='search'),
]
