# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='description',
            field=models.TextField(default='My hood is the best'),
        ),
    ]