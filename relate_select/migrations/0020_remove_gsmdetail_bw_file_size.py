# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-07 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relate_select', '0019_gsmdetail_gsm_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gsmdetail',
            name='bw_file_size',
        ),
    ]
