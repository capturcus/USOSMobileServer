# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('usosid', models.IntegerField()),
            ],
            options={
                'ordering': ('usosid',),
            },
        ),
    ]
