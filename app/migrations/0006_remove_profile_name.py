# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 13:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_neighbourhood_hood_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
