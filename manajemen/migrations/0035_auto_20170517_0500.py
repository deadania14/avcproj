# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-17 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen', '0034_administrasi_nominal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrasi',
            name='image',
            field=models.ImageField(null=True, upload_to='images/bukti_payments'),
        ),
    ]