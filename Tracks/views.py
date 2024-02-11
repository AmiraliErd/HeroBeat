from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from Tracks.models import Track, Album, Category, Artist, Comment, Video
from django.core.paginator import Paginator

# Create your views here.


def tracks_list(request):
    tracks = Track.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(tracks, 42)
    page_list = paginator.get_page(page_number)
    return render(request, 'Tracks/music.html', context={'tracks_list': page_list})


def albums_list(request):
    albums = Album.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(albums, 42)
    page_list = paginator.get_page(page_number)
    return render(request, 'Tracks/Album.html', context={'albums_list': page_list})


def track_details(request, slug):
    track = get_object_or_404(Track, slug=slug)
    recent_tracks = Track.objects.all()[:6]

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')

        Comment.objects.create(body=body, firstname=firstname, lastname=lastname, track=track, parent_id=parent_id)

    return render(request, 'Tracks/music_details.html', context={'track': track, 'recent_tracks':recent_tracks})


def album_details(request, slug):
    album = get_object_or_404(Album, slug=slug)
    recent_albums = Album.objects.all()[:6]
    tracks = album.tracks.all()

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')

        Comment.objects.create(body=body, firstname=firstname, lastname=lastname, album=album, parent_id=parent_id)

    return render(request, 'Tracks/Album_detail.html', context={'album': album, 'tracks_list': tracks, 'recent_albums': recent_albums})


def album_320(request, slug):
    album = get_object_or_404(Album, slug=slug)
    tracks = album.tracks.all()
    return render(request, 'Tracks/album_320.html', context={'tracks_list': tracks, 'album': album})


def album_128(request, slug):
    album = get_object_or_404(Album, slug=slug)
    tracks = album.tracks.all()
    return render(request, 'Tracks/album_128.html', context={'tracks_list': tracks, 'album': album})


def artist_details(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    videos = artist.videos.all()
    albums = artist.albums.all()
    single_tracks = artist.tracks.filter(single=True)
    return render(request, 'Tracks/artist_details.html', context={'artist': artist, 'albums': albums, 'single_tracks': single_tracks, 'videos': videos})



def search(request):
    q = request.GET.get('q')
    lookups = Q(farsi_name__icontains=q) | Q(name__icontains=q)
    tracks = Track.objects.filter(lookups)
    albums = Album.objects.filter(lookups)
    return render(request, 'Tracks/search_result.html', {'tracks_list': tracks, 'albums_list': albums})









