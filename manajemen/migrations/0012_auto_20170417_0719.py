# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen', '0011_administrasi_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrasi',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='kelas',
            name='updated_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
