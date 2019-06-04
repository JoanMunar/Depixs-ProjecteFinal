# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180521_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colleges',
            options={'verbose_name': 'Universidad', 'verbose_name_plural': 'Universidades'},
        ),
        migrations.AlterModelOptions(
            name='studies',
            options={'verbose_name': 'Estudio', 'verbose_name_plural': 'Estudios'},
        ),
        migrations.RemoveField(
            model_name='colleges',
            name='colleges',
        ),
        migrations.RemoveField(
            model_name='studies',
            name='studies',
        ),
        migrations.AddField(
            model_name='colleges',
            name='name',
            field=models.CharField(default='pp', max_length=100, verbose_name=b'Universidades:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studies',
            name='name',
            field=models.CharField(default='pp', max_length=100, verbose_name=b'Estudios:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Colleges', verbose_name=b'Universidad'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, ''), (2, 'Mujer'), (1, 'Hombre')], default=0, verbose_name=b'G\xc3\xa9nero:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=0, verbose_name=b'Puntos:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preference',
            field=models.IntegerField(choices=[(0, ''), (3, 'Ambos'), (2, 'Solo chicas'), (1, 'Solo chicos')], default=0, verbose_name=b'Preferencia:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Studies', verbose_name=b'Estudios:'),
        ),
    ]