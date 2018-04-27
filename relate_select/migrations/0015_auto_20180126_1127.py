# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relate_select', '0014_auto_20171221_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='date_time',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='document',
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='gse_id',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='gsm_id',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='oganization',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
