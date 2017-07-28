# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='conector',
            field=models.CharField(default=b'SOME STRING', max_length=100),
        ),
    ]
