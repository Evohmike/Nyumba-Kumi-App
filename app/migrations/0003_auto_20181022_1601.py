# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_neighbourhood_hood_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='health',
            field=models.CharField(default='071000000', max_length=15),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='police',
            field=models.CharField(default='9999', max_length=15),
        ),
    ]
