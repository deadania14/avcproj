# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 02:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen', '0026_auto_20170510_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('note', models.TextField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('updated_date', models.DateField(default=datetime.datetime(2017, 5, 13, 2, 25, 29, 462613, tzinfo=utc))),
            ],
        ),
    ]
