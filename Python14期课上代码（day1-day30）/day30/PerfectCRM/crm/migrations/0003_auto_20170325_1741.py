# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_userprofile_roles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': '客户信息表', 'verbose_name_plural': '客户信息表'},
        ),
        migrations.AddField(
            model_name='customer',
            name='graduated',
            field=models.BooleanField(default=False),
        ),
    ]
