# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20141223_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='finish_year',
            field=models.SmallIntegerField(null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb0\xd1\x81\xd0\xbf\xd0\xb0\xd0\xb4\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='band',
            name='start_year',
            field=models.SmallIntegerField(null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xbe\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
    ]
