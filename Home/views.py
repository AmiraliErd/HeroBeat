from django.shortcuts import render, get_object_or_404
from Tracks.models import Track, Album, Podcast, Artist


# Create your views here.


def recent(request):
    recent_tracks = Track.objects.all()[:6]
    recent_albums = Album.objects.all()[:6]
    recent_podcasts = Podcast.objects.all()[:6]
    artists_list = Artist.objects.all()[:7]
    return render(request, 'Home/index.html', context={'recent_tracks': recent_tracks, 'artists_list': artists_list, 'recent_albums': recent_albums, 'recent_podcasts': recent_podcasts})
