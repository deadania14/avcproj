# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen', '0013_kelas_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='practiceattendance',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
