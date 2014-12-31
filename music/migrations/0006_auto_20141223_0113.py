# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20141221_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0440\u043e\u043b\u044c',
                'verbose_name_plural': '\u0440\u043e\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artist',
            name='role',
            field=models.ForeignKey(related_name='artists', verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xbb\xd1\x8c', blank=True, to='music.Role', null=True),
            preserve_default=True,
        ),
    ]
