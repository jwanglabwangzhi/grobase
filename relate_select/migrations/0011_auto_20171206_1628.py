# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relate_select', '0010_auto_20171206_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='specie_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
