# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_auto_20170602_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='conector',
            new_name='link',
        ),
    ]
