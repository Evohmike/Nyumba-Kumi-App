# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 19:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_name', models.CharField(max_length=30)),
                ('neighbourhood_location', models.CharField(blank=True, choices=[('Kiambu', 'Kiambu'), ('Kasarani', 'Kasarani'), ('Syokimau', 'Syokimau'), ('Makadara', 'Makadara'), ('Roysambu', 'Roysambu'), ('Umoja', 'Umoja'), ('Buruburu', 'Buruburu'), ('Karen', 'Karen'), ('Lavington', 'Lavongton'), ('Kibera', 'Kibera')], default=0, max_length=200, null=True)),
                ('population', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(default='Anonymous')),
                ('profile_pic', models.ImageField(blank=True, default=0, null=True, upload_to='picture/')),
                ('bio', models.TextField(blank=True, default='my bio', max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
