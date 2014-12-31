# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20141221_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='pic',
            field=models.ImageField(upload_to=music.models.album_cover_rename, null=True, verbose_name=b'\xd0\x9e\xd0\xb1\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xba\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
