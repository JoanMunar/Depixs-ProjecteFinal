# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_chat_attempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='carousel',
            field=models.ManyToManyField(blank=True, related_name='user_carousel', to='core.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, ''), (2, 'Mujer'), (1, 'Hombre')], default=0, verbose_name=b'G\xc3\xa9nero'),
        ),
        migrations.AlterField(
            model_name='user',
            name='invited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_invited_by', to='core.User', verbose_name=b'Invitado por'),
        ),
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=0, verbose_name=b'Puntos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preference',
            field=models.IntegerField(choices=[(3, 'Ambos'), (2, 'Solo chicas'), (1, 'Solo chicos')], default=3, verbose_name=b'Preferencia'),
        ),
        migrations.AlterField(
            model_name='user',
            name='study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Studies', verbose_name=b'Estudios'),
        ),
    ]
