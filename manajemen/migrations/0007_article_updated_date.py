# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-06 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen', '0006_auto_20170406_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]