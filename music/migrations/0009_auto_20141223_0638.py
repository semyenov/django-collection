# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20141223_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='finish_year',
            field=models.SmallIntegerField(null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb0\xd1\x81\xd0\xbf\xd0\xb0\xd0\xb4\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
