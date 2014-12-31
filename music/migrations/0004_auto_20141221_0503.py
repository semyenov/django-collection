# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_track_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='number',
            field=models.SmallIntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80'),
            preserve_default=True,
        ),
    ]
