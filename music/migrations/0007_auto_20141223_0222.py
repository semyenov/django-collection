# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20141223_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='pic',
            field=models.ImageField(upload_to=music.models.band_pic_rename, null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=True,
        ),
    ]
