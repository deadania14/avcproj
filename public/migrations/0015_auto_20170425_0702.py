# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0014_auto_20170425_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsvariable',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
    ]