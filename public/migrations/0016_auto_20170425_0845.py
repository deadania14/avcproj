# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0015_auto_20170425_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tipe_user',
            field=models.CharField(choices=[('member', 'Member'), ('tutor', 'Tutor'), ('ketua/wakil', 'Ketua/Wakil'), ('sekretaris', 'Sekretaris'), ('bendahara', 'Bendahara'), ('hpd', 'HPD'), ('psdm', 'PSDM'), ('inventaris', 'Inventaris'), ('program', 'Program')], default='member', max_length=20),
        ),
    ]
