# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_post_conector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conector',
            field=models.CharField(default=b'www.google.com', max_length=100),
        ),
    ]
