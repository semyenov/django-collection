# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_album_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='category',
            field=models.CharField(default=b'LP', max_length=10, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', choices=[(b'LP', b'LP'), (b'EP', b'EP'), (b'SINGLE', b'SINGLE')]),
            preserve_default=True,
        ),
    ]
