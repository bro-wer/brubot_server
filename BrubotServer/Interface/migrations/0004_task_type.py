# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-04 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0003_auto_20181004_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.CharField(choices=[('UD', 'Undefined'), ('TR', 'Torrent')], default='Undefined', max_length=5),
        ),
    ]