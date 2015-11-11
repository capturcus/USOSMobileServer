# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastname',
        ),
        migrations.AddField(
            model_name='student',
            name='deviceid',
            field=models.CharField(default='no', max_length=100),
            preserve_default=False,
        ),
    ]
