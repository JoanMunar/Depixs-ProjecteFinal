# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='points',
        ),
    ]
