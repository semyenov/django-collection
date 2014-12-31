# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20141223_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd1\x85\xd0\xbe\xd0\xb4\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
