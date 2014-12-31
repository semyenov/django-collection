# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20141221_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='number',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80'),
            preserve_default=True,
        ),
    ]
