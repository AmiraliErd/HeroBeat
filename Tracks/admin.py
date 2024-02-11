from django.contrib import admin
from .models import Track, Album, Artist, Category, Comment, Podcast, Video

admin.site.site_header = "HeroBeat Panel"
admin.site.site_title = "HeroBeat Panel"
admin.site.index_title = "مدیریت سایت"

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'show_image')
    list_filter = ('single',)
    search_fields = ('name', 'farsi_name')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_image')
    search_fields = ('name', 'farsi_name')


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'show_image')
    search_fields = ('name', 'farsi_name')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('name',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_image')
    search_fields = ('name', 'farsi_name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (f'firstname', '__str__')
    search_fields = ('firstname', 'lastname', 'body')


admin.site.register(Category)
