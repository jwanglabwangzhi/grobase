# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relate_select', '0004_auto_20171206_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='relate_select.Album')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.RemoveField(
            model_name='process',
            name='source_name',
        ),
        migrations.RemoveField(
            model_name='sources',
            name='specie_name',
        ),
        migrations.DeleteModel(
            name='Process',
        ),
        migrations.DeleteModel(
            name='Sources',
        ),
        migrations.DeleteModel(
            name='Species',
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([('album', 'order')]),
        ),
    ]
