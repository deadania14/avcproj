# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-04 04:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen', '0022_article_is_mainarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
