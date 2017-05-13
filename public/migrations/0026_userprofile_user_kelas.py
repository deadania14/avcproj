# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen', '0026_auto_20170510_1527'),
        ('public', '0025_remove_userprofile_pobirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_kelas',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kelas', to='manajemen.Kelas'),
        ),
    ]