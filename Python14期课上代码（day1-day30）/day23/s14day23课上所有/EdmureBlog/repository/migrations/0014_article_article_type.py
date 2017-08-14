# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-13 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0013_auto_20170113_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.IntegerField(choices=[(1, 'Python'), (2, 'Linux'), (3, 'OpenStack'), (4, 'GoLang')], default=None),
        ),
    ]
