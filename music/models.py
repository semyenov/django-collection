#-*- coding: utf-8 -*-
from django.db import models
import os


def album_cover_rename(instance, filename):
    path = 'album_pics'
    print(instance)
    ext = filename.split('.')[-1]
    filename = '%s%s.%s' % (instance.title, instance.id, ext)
    return os.path.join(path, filename)


def band_pic_rename(instance, filename):
    path = 'band_pics'
    print(instance)
    ext = filename.split('.')[-1]
    filename = '%s%s.%s' % (instance.name, instance.id, ext)
    return os.path.join(path, filename)


RATING_CHOICES = (
        (1, 'Ужасно'),
        (2, 'Плохо'),
        (3, 'Средне'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
)

CATEGORY_CHOICES = (
        ('LP', 'LP'),
        ('EP', 'EP'),
        ('SINGLE', 'SINGLE'),
)


class Role(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'

    def __unicode__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    role = models.ForeignKey(Role, related_name='artists', verbose_name='Роль', null=True, blank=True)
    bio = models.TextField(verbose_name='Биография', blank=True, null=True)
    pic = models.ImageField(upload_to='artist_pics', verbose_name='Фотография', blank=True, null=True)

    class Meta:
        verbose_name = 'музыкант'
        verbose_name_plural = 'музыканты'

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)


class Band(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    bio = models.TextField(verbose_name='История', blank=True, null=True)
    start_year = models.SmallIntegerField(verbose_name='Год основания', null=True)
    finish_year = models.SmallIntegerField(verbose_name='Год распада', null=True, blank=True)
    pic = models.ImageField(upload_to=band_pic_rename, verbose_name='Фотография', blank=True, null=True)
    artists = models.ManyToManyField(Artist, related_name='bands', verbose_name='Участники')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __unicode__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    rating = models.SmallIntegerField(choices=RATING_CHOICES, verbose_name='Оценка')
    year = models.DateField(verbose_name='Дата выхода', blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name='Категория', default='LP')
    bio = models.TextField(verbose_name='Описание', blank=True, null=True)
    pic = models.ImageField(upload_to=album_cover_rename, verbose_name='Обложка', blank=True, null=True)
    band = models.ForeignKey(Band, related_name='albums', verbose_name='Группа')

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

    def __unicode__(self):
        return self.title


class Track(models.Model):
    number = models.SmallIntegerField(verbose_name='Номер')
    title = models.CharField(max_length=100, verbose_name='Название')
    rating = models.SmallIntegerField(choices=RATING_CHOICES, verbose_name='Оценка')
    lyric = models.TextField(verbose_name='Текст', blank=True, null=True)
    album = models.ForeignKey(Album, related_name='tracks', verbose_name='Альбом')

    class Meta:
        verbose_name = 'песня'
        verbose_name_plural = 'песни'

    def __unicode__(self):
        return '%s: %s' % (self.album, self.title)