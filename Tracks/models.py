from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    farsi_title = models.CharField(null=True, blank=True, max_length=40)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    class Meta:
      verbose_name = 'سبک'
      verbose_name_plural = 'سبک ها'


class Artist(models.Model):
    name = models.CharField(max_length=50)
    farsi_name = models.CharField(null=True, blank=True, max_length=40)
    image = models.ImageField(upload_to='artists')
    banner = models.ImageField(upload_to='artists', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Artist, self).save()

    class Meta:
      verbose_name = 'هنرمند'
      verbose_name_plural = 'هنرمندان'

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="60px">')
        else:
            return format_html('<h3>تصویر ندارد</h3>')


class Album(models.Model):
    name = models.CharField(max_length=50)
    farsi_name = models.CharField(null=True, blank=True, max_length=40)
    image = models.ImageField(upload_to='tracks')
    artist = models.ManyToManyField(Artist, related_name="albums")
    created = models.DateTimeField(auto_now_add=True)
    file_128 = models.FileField(upload_to='files', null=True)
    file_320 = models.FileField(upload_to='files', null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Album, self).save()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'آلبوم'
        verbose_name_plural = 'آلبوم ها'

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="100px" height="100px">')
        else:
            return format_html('<h3>تصویر ندارد</h3>')


class Track(models.Model):
    name = models.CharField(null=True, blank=True, max_length=40)
    farsi_name = models.CharField(null=True, blank=True, max_length=40)
    category = models.ManyToManyField(Category, related_name="tracks")
    artist = models.ManyToManyField(Artist, related_name="tracks")
    single = models.BooleanField(default=True, verbose_name='سینگل ترک')
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE, related_name="tracks")
    created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='tracks', null=True, blank=True)
    quality_320 = models.FileField(upload_to='files',  null=True, blank=True)
    quality_128 = models.FileField(upload_to='files', null=True, blank=True)
    lyric = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Track, self).save()

    def __str__(self):
        return f"{self.name} - {self.artist.first()}"

    class Meta:
        ordering = ('-created',)
        verbose_name = 'موزیک'
        verbose_name_plural = 'موزیک ها'

    def show_image(self):
        if self.cover:
            return format_html(f'<img src="{self.cover.url}" width="100px" height="100px">')
        else:
            return format_html('<h3>تصویر ندارد</h3>')

class Podcast(models.Model):
    name = models.CharField(null=True, blank=True, max_length=40)
    farsi_name = models.CharField(null=True, blank=True, max_length=40)
    artist = models.ManyToManyField(Artist, related_name="podcasts")
    created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='podcasts', null=True, blank=True)
    file = models.FileField(upload_to='files',  null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Podcast, self).save()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = 'پادکست'
        verbose_name_plural = 'پادکست ها'

    def show_image(self):
        if self.cover:
            return format_html(f'<img src="{self.cover.url}" width="100px" height="100px">')
        else:
            return format_html('<h3>تصویر ندارد</h3>')


class Video (models.Model):
    name = models.CharField(null=True, blank=True, max_length=40)
    artist = models.ManyToManyField(Artist, related_name="videos")
    file = models.FileField(upload_to='videos', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Video, self).save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'موزیک ویدیو'
        verbose_name_plural = 'موزیک ویدیو ها'


class Comment(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:30]

    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه ها'