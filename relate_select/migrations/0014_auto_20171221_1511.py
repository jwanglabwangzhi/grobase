# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relate_select', '0013_auto_20171212_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sources',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
