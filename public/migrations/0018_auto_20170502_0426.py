# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-02 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import public.validators


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0017_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_have_kelas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='attachment',
            field=models.FileField(blank=True, upload_to='files/events', validators=[public.validators.validate_file_extension], verbose_name='proposal atau undangan'),
        ),
    ]
