# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('rating', models.SmallIntegerField(verbose_name=b'\xd0\x9e\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb0', choices=[(1, b'\xd0\xa3\xd0\xb6\xd0\xb0\xd1\x81\xd0\xbd\xd0\xbe'), (2, b'\xd0\x9f\xd0\xbb\xd0\xbe\xd1\x85\xd0\xbe'), (3, b'\xd0\xa1\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5'), (4, b'\xd0\xa5\xd0\xbe\xd1\x80\xd0\xbe\xd1\x88\xd0\xbe'), (5, b'\xd0\x9e\xd1\x82\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe')])),
                ('bio', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('pic', models.ImageField(upload_to=b'album_pics', null=True, verbose_name=b'\xd0\x9e\xd0\xb1\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xba\xd0\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u0430\u043b\u044c\u0431\u043e\u043c',
                'verbose_name_plural': '\u0430\u043b\u044c\u0431\u043e\u043c\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('surname', models.CharField(max_length=100, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('bio', models.TextField(null=True, verbose_name=b'\xd0\x91\xd0\xb8\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f', blank=True)),
                ('pic', models.ImageField(upload_to=b'artist_pics', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f', blank=True)),
            ],
            options={
                'verbose_name': '\u043c\u0443\u0437\u044b\u043a\u0430\u043d\u0442',
                'verbose_name_plural': '\u043c\u0443\u0437\u044b\u043a\u0430\u043d\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('bio', models.TextField(null=True, verbose_name=b'\xd0\x98\xd1\x81\xd1\x82\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True)),
                ('pic', models.ImageField(upload_to=b'band_pics', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f', blank=True)),
                ('artists', models.ManyToManyField(related_name='bands', verbose_name=b'\xd0\xa3\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8', to='music.Artist')),
            ],
            options={
                'verbose_name': '\u0433\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0433\u0440\u0443\u043f\u043f\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('rating', models.SmallIntegerField(verbose_name=b'\xd0\x9e\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb0', choices=[(1, b'\xd0\xa3\xd0\xb6\xd0\xb0\xd1\x81\xd0\xbd\xd0\xbe'), (2, b'\xd0\x9f\xd0\xbb\xd0\xbe\xd1\x85\xd0\xbe'), (3, b'\xd0\xa1\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5'), (4, b'\xd0\xa5\xd0\xbe\xd1\x80\xd0\xbe\xd1\x88\xd0\xbe'), (5, b'\xd0\x9e\xd1\x82\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe')])),
                ('lyric', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('album', models.ForeignKey(related_name='tracks', verbose_name=b'\xd0\x90\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc', to='music.Album')),
            ],
            options={
                'verbose_name': '\u043f\u0435\u0441\u043d\u044f',
                'verbose_name_plural': '\u043f\u0435\u0441\u043d\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(related_name='albums', verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb0', to='music.Band'),
            preserve_default=True,
        ),
    ]
